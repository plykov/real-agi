#!/usr/bin/env python3
"""Windows loopback audio capture & transcription agent.

Captures whatever Windows is currently playing (system audio, "what you hear")
via WASAPI loopback, records it to a WAV file, and transcribes it locally with
faster-whisper. No virtual audio cables or Stereo Mix needed.

Usage:
    python audio_agent.py devices                 # list capturable output devices
    python audio_agent.py run                     # record until silence, then transcribe
    python audio_agent.py record -o clip.wav      # record only
    python audio_agent.py transcribe clip.wav     # transcribe an existing file

Requires Windows. See README.md for setup.
"""

from __future__ import annotations

import argparse
import array
import datetime as dt
import math
import sys
import time
import wave
from pathlib import Path

SAMPLE_WIDTH = 2  # bytes, 16-bit PCM
CHUNK_SECONDS = 0.1  # RMS window per stream read
DEFAULT_SILENCE_DBFS = -45.0


def _require_windows() -> None:
    if sys.platform != "win32":
        sys.exit("This agent captures audio via WASAPI loopback and only runs on Windows.")


def _pyaudio():
    try:
        import pyaudiowpatch as pyaudio
    except ImportError:
        sys.exit(
            "pyaudiowpatch is not installed. Run: pip install PyAudioWPatch\n"
            "(Windows-only package; see README.md)"
        )
    return pyaudio


def _find_loopback_device(p, pyaudio, device_index: int | None):
    """Return the loopback device info dict to record from.

    If device_index is given it must be a loopback device (see `devices`).
    Otherwise the loopback twin of the default output device is used.
    """
    if device_index is not None:
        info = p.get_device_info_by_index(device_index)
        if not info.get("isLoopbackDevice", False):
            sys.exit(
                f"Device {device_index} ({info['name']}) is not a loopback device. "
                "Run `python audio_agent.py devices` to list valid ones."
            )
        return info

    wasapi_info = p.get_host_api_info_by_type(pyaudio.paWASAPI)
    default_speakers = p.get_device_info_by_index(wasapi_info["defaultOutputDevice"])
    if default_speakers.get("isLoopbackDevice", False):
        return default_speakers
    for loopback in p.get_loopback_device_info_generator():
        if default_speakers["name"] in loopback["name"]:
            return loopback
    sys.exit(
        f"No loopback device found for default output '{default_speakers['name']}'. "
        "Run `python audio_agent.py devices` and pass one explicitly with --device."
    )


def rms_dbfs(frames: bytes) -> float:
    """RMS level of a 16-bit PCM chunk in dBFS (0 = full scale, -120 = silence)."""
    samples = array.array("h")
    samples.frombytes(frames[: len(frames) - len(frames) % SAMPLE_WIDTH])
    if not samples:
        return -120.0
    rms = math.sqrt(sum(s * s for s in samples) / len(samples))
    if rms <= 0:
        return -120.0
    return 20 * math.log10(rms / 32768.0)


def cmd_devices(_args) -> None:
    _require_windows()
    pyaudio = _pyaudio()
    with pyaudio.PyAudio() as p:
        wasapi_info = p.get_host_api_info_by_type(pyaudio.paWASAPI)
        default_out = wasapi_info["defaultOutputDevice"]
        print("WASAPI loopback devices (use --device <index> with `record`/`run`):\n")
        for info in p.get_loopback_device_info_generator():
            marker = "  <- default output" if default_out >= 0 and str(
                p.get_device_info_by_index(default_out)["name"]
            ) in str(info["name"]) else ""
            print(
                f"  [{info['index']:3d}] {info['name']}  "
                f"({int(info['defaultSampleRate'])} Hz, {info['maxInputChannels']} ch){marker}"
            )


def record_loopback(
    out_path: Path,
    device_index: int | None,
    max_seconds: float,
    silence_timeout: float,
    silence_dbfs: float,
    wait_for_sound: float,
) -> Path:
    """Record system playback to a WAV file.

    Stops on the first of: Ctrl+C, `max_seconds` elapsed, or — once sound has
    been heard — `silence_timeout` seconds of continuous silence. If nothing
    plays within `wait_for_sound` seconds, gives up.
    """
    _require_windows()
    pyaudio = _pyaudio()

    with pyaudio.PyAudio() as p:
        device = _find_loopback_device(p, pyaudio, device_index)
        rate = int(device["defaultSampleRate"])
        channels = int(device["maxInputChannels"])
        chunk_frames = max(1, int(rate * CHUNK_SECONDS))

        print(f"Recording from: {device['name']} ({rate} Hz, {channels} ch)")
        print(
            f"Stops after {silence_timeout:.0f}s of silence (< {silence_dbfs:.0f} dBFS), "
            f"{max_seconds:.0f}s max, or Ctrl+C."
        )

        frames: list[bytes] = []
        heard_sound = False
        silent_for = 0.0
        started = time.monotonic()

        stream = p.open(
            format=pyaudio.paInt16,
            channels=channels,
            rate=rate,
            input=True,
            input_device_index=device["index"],
            frames_per_buffer=chunk_frames,
        )
        try:
            print("Listening... play the audio clip now.")
            while True:
                data = stream.read(chunk_frames, exception_on_overflow=False)
                frames.append(data)
                elapsed = time.monotonic() - started
                level = rms_dbfs(data)

                if level >= silence_dbfs:
                    if not heard_sound:
                        print("Sound detected, recording.")
                    heard_sound = True
                    silent_for = 0.0
                else:
                    silent_for += CHUNK_SECONDS

                if elapsed >= max_seconds:
                    print(f"Max duration ({max_seconds:.0f}s) reached.")
                    break
                if heard_sound and silent_for >= silence_timeout:
                    print(f"{silence_timeout:.0f}s of silence, stopping.")
                    break
                if not heard_sound and elapsed >= wait_for_sound:
                    print(f"No sound within {wait_for_sound:.0f}s, giving up.")
                    break
        except KeyboardInterrupt:
            print("\nStopped by user.")
        finally:
            stream.stop_stream()
            stream.close()

        if not heard_sound:
            sys.exit("Nothing was recorded (only silence captured). Is audio playing?")

        out_path.parent.mkdir(parents=True, exist_ok=True)
        with wave.open(str(out_path), "wb") as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(SAMPLE_WIDTH)
            wf.setframerate(rate)
            wf.writeframes(b"".join(frames))

        duration = len(frames) * CHUNK_SECONDS
        print(f"Saved {duration:.1f}s of audio to {out_path}")
        return out_path


def _format_srt_time(seconds: float) -> str:
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def transcribe_file(
    audio_path: Path,
    model_size: str,
    language: str | None,
    write_srt: bool,
) -> Path:
    """Transcribe an audio file with faster-whisper; writes .txt (and optionally .srt)."""
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        sys.exit("faster-whisper is not installed. Run: pip install faster-whisper")

    if not audio_path.exists():
        sys.exit(f"Audio file not found: {audio_path}")

    print(f"Loading Whisper model '{model_size}' (first run downloads it)...")
    model = WhisperModel(model_size, device="auto", compute_type="auto")

    print(f"Transcribing {audio_path}...")
    segments, info = model.transcribe(
        str(audio_path),
        language=language,
        vad_filter=True,
    )
    print(f"Detected language: {info.language} (p={info.language_probability:.2f})")

    lines: list[str] = []
    srt_blocks: list[str] = []
    for i, seg in enumerate(segments, start=1):
        text = seg.text.strip()
        print(f"  [{seg.start:6.1f}s -> {seg.end:6.1f}s] {text}")
        lines.append(text)
        srt_blocks.append(
            f"{i}\n{_format_srt_time(seg.start)} --> {_format_srt_time(seg.end)}\n{text}\n"
        )

    txt_path = audio_path.with_suffix(".txt")
    txt_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Transcript saved to {txt_path}")

    if write_srt:
        srt_path = audio_path.with_suffix(".srt")
        srt_path.write_text("\n".join(srt_blocks), encoding="utf-8")
        print(f"Subtitles saved to {srt_path}")

    return txt_path


def _default_output_path(out_dir: Path) -> Path:
    stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    return out_dir / f"capture_{stamp}.wav"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Capture Windows playback audio (WASAPI loopback) and transcribe it."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("devices", help="List WASAPI loopback devices").set_defaults(func=cmd_devices)

    def add_record_args(sp):
        sp.add_argument("-o", "--output", type=Path, help="Output WAV path")
        sp.add_argument("--out-dir", type=Path, default=Path("recordings"),
                        help="Directory for auto-named recordings (default: recordings/)")
        sp.add_argument("--device", type=int, help="Loopback device index (see `devices`)")
        sp.add_argument("--max-seconds", type=float, default=600,
                        help="Hard recording limit in seconds (default: 600)")
        sp.add_argument("--silence-timeout", type=float, default=3.0,
                        help="Stop after this many seconds of silence (default: 3)")
        sp.add_argument("--silence-dbfs", type=float, default=DEFAULT_SILENCE_DBFS,
                        help=f"Silence threshold in dBFS (default: {DEFAULT_SILENCE_DBFS})")
        sp.add_argument("--wait-for-sound", type=float, default=30,
                        help="Give up if no sound starts within this many seconds (default: 30)")

    def add_transcribe_args(sp):
        sp.add_argument("--model", default="small",
                        help="Whisper model size: tiny/base/small/medium/large-v3 (default: small)")
        sp.add_argument("--language", default=None,
                        help="Language code, e.g. en, ru, nl (default: auto-detect)")
        sp.add_argument("--srt", action="store_true", help="Also write an .srt subtitle file")

    p_record = sub.add_parser("record", help="Record system playback to WAV")
    add_record_args(p_record)

    p_transcribe = sub.add_parser("transcribe", help="Transcribe an existing audio file")
    p_transcribe.add_argument("audio", type=Path, help="Audio file to transcribe")
    add_transcribe_args(p_transcribe)

    p_run = sub.add_parser("run", help="Record system playback, then transcribe it")
    add_record_args(p_run)
    add_transcribe_args(p_run)

    args = parser.parse_args()

    if args.command == "devices":
        args.func(args)
        return

    if args.command == "transcribe":
        transcribe_file(args.audio, args.model, args.language, args.srt)
        return

    out_path = args.output or _default_output_path(args.out_dir)
    wav = record_loopback(
        out_path=out_path,
        device_index=args.device,
        max_seconds=args.max_seconds,
        silence_timeout=args.silence_timeout,
        silence_dbfs=args.silence_dbfs,
        wait_for_sound=args.wait_for_sound,
    )
    if args.command == "run":
        transcribe_file(wav, args.model, args.language, args.srt)


if __name__ == "__main__":
    main()
