#!/usr/bin/env python3
"""M1 Harvest CLI.

Live:     python run_harvest.py --postcode 5038
Fixture:  python run_harvest.py --postcode 5038 --fixture fixtures/overpass_5038_synthetic.json
"""

import argparse
import sys

from localsite.harvest import run


def main() -> int:
    ap = argparse.ArgumentParser(description="LocalSite Agent — M1 Harvest")
    ap.add_argument("--postcode", default="5038", help="4-digit postcode area")
    ap.add_argument("--city", default="Tilburg")
    ap.add_argument("--db", default="localsite.db")
    ap.add_argument(
        "--fixture",
        help="Path to an Overpass-shaped JSON file (offline / synthetic run)",
    )
    args = ap.parse_args()

    report = run(
        db_path=args.db,
        postcode4=args.postcode,
        city=args.city,
        fixture=args.fixture,
    )

    w = 34
    print(f"\n=== M1 Harvest report — {args.city} {args.postcode} "
          f"[{report['source']}] ===\n")
    print(f"{'Harvested this run':<{w}}{report['harvested_this_run']}")
    print(f"{'Total records in DB':<{w}}{report['total_records']}")
    print(f"{'KvK matched / unmatched':<{w}}"
          f"{report['kvk_matched']} / {report['kvk_unmatched']}")
    print(f"\n{'Active (passed F1–F4)':<{w}}{report['active']}")
    print(f"{'Parked in nurture-later (F3)':<{w}}{report['nurture']}")
    print("\nExclusion breakdown:")
    labels = {
        "F1": "F1 NMI set",
        "F2": "F2 status ≠ actief",
        "F3": "F3 <12 months (parked)",
        "F4": "F4 chain/franchise",
    }
    for code, n in report["exclusions"].items():
        print(f"  {labels.get(code, code):<{w - 2}}{n}")
    if not report["exclusions"]:
        print("  (none)")
    print("\nChannel split (active records):")
    for channel, n in report["channel_split"].items():
        print(f"  {channel:<{w - 2}}{n}")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
