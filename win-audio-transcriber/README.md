# win-audio-transcriber

A Windows agent that captures the sound your PC is **playing back** (system audio, "what you hear"), records it to a WAV file, and transcribes it to text — fully offline.

It uses **WASAPI loopback** capture, so it hears exactly what goes to your speakers/headphones. No microphone, no virtual audio cable, no "Stereo Mix" needed. Transcription runs locally via [faster-whisper](https://github.com/SYSTRAN/faster-whisper); nothing is uploaded anywhere.

## Requirements

- Windows 10/11
- Python 3.9–3.12 (64-bit) — [PyAudioWPatch](https://github.com/s0d3s/PyAudioWPatch) ships prebuilt wheels for these versions
- ~1 GB of disk for the default Whisper model (downloaded automatically on first transcription)

## Setup

```powershell
cd win-audio-transcriber
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

**One-shot: record what's playing, then transcribe it** (the main workflow):

```powershell
python audio_agent.py run
```

Start it, then play your audio clip. The agent waits for sound, records, stops automatically after 3 seconds of silence, saves a WAV to `recordings/`, and writes the transcript next to it as a `.txt` file (segments are also printed live).

**Record only:**

```powershell
python audio_agent.py record -o clip.wav
```

**Transcribe an existing file** (WAV/MP3/M4A/etc.):

```powershell
python audio_agent.py transcribe clip.wav --srt
```

**List capturable output devices** (if you play audio on a non-default device):

```powershell
python audio_agent.py devices
python audio_agent.py run --device 14
```

## Useful options

| Option | Default | Meaning |
|---|---|---|
| `--silence-timeout` | `3` | Stop after this many seconds of silence |
| `--silence-dbfs` | `-45` | Silence threshold; raise (e.g. `-35`) if background hiss keeps it recording |
| `--max-seconds` | `600` | Hard recording limit |
| `--wait-for-sound` | `30` | Give up if nothing plays within this window |
| `--model` | `small` | Whisper size: `tiny`, `base`, `small`, `medium`, `large-v3` — bigger = more accurate, slower |
| `--language` | auto | Force a language, e.g. `--language ru` or `--language nl` |
| `--srt` | off | Also write timestamped `.srt` subtitles |

Press **Ctrl+C** at any time to stop recording early; the captured audio is still saved and transcribed.

## How it works

1. **Capture** — Windows' WASAPI API exposes every output device in *loopback* mode, meaning you can open it as an input and read back the exact PCM stream being rendered to it. `PyAudioWPatch` (a PyAudio fork) surfaces these loopback devices; the agent picks the one matching your default speakers.
2. **Record** — 100 ms chunks are read and their RMS level (dBFS) is measured. Recording starts immediately, and stops once sound has been heard followed by sustained silence — so you get exactly the clip, hands-free.
3. **Transcribe** — the WAV is fed to faster-whisper with voice-activity filtering; the transcript is written as plain text (and optionally SRT with timestamps).

## Notes

- If your clip plays on Bluetooth headphones or another non-default device, list devices and pass `--device`.
- Transcription accuracy: `small` is a good speed/quality balance for clean speech; use `medium` or `large-v3` for noisy audio or heavy accents. On a machine with an NVIDIA GPU, faster-whisper uses CUDA automatically if the CUDA libraries are present.
- DRM-protected streams that use protected audio paths cannot be loopback-captured by any user-mode tool; everything else (browser audio, media players, calls) works.
