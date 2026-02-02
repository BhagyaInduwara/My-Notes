#!/usr/bin/env python3
"""
Fetch a GitHub user's contribution calendar and report how many empty days
(within a fixed window) need a contribution to reach ~80% fill.

Usage:
    python scripts/check_graph.py [username]

If no username is given, GITHUB_USERNAME below is used.
"""

import json
import math
import re
import sys
import urllib.request
import urllib.error
from datetime import date, datetime, timedelta
from pathlib import Path

GITHUB_USERNAME = "BhagyaInduwara"
WINDOW_START = date(2026, 2, 1)
TARGET_FILL_RATIO = 0.80

SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_PATH = SCRIPT_DIR / "empty_days.json"

CONTRIBUTIONS_URL = "https://github.com/users/{username}/contributions"

# Matches any tag that carries both data-date and data-level, regardless of
# which attribute comes first or what else is on the tag.
TAG_RE = re.compile(r"<[^>]*data-date=\"[^\"]*\"[^>]*>|<[^>]*data-level=\"[^\"]*\"[^>]*>")
DATE_RE = re.compile(r'data-date="(\d{4}-\d{2}-\d{2})"')
LEVEL_RE = re.compile(r'data-level="(\d+)"')


def fetch_contributions_html(username: str) -> str:
    url = CONTRIBUTIONS_URL.format(username=username)
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0 Safari/537.36"
            )
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        raise SystemExit(f"Failed to fetch contributions page: HTTP {exc.code}") from exc
    except urllib.error.URLError as exc:
        raise SystemExit(f"Failed to fetch contributions page: {exc.reason}") from exc


def parse_days(html: str) -> dict:
    """Return {date: level} for every day found in the calendar HTML."""
    days = {}
    for match in TAG_RE.finditer(html):
        tag = match.group(0)
        date_match = DATE_RE.search(tag)
        level_match = LEVEL_RE.search(tag)
        if date_match and level_match:
            day = datetime.strptime(date_match.group(1), "%Y-%m-%d").date()
            days[day] = int(level_match.group(1))
    return days


def main():
    username = sys.argv[1] if len(sys.argv) > 1 else GITHUB_USERNAME
    today = date.today()

    if WINDOW_START > today:
        raise SystemExit("WINDOW_START is in the future; nothing to check.")

    html = fetch_contributions_html(username)
    all_days = parse_days(html)

    window_days = {
        day: level
        for day, level in all_days.items()
        if WINDOW_START <= day <= today
    }

    # Guard against GitHub not returning every calendar day in the window
    # (e.g. window predates what the endpoint serves back).
    total_days = (today - WINDOW_START).days + 1
    known_days = len(window_days)

    filled_days = sum(1 for level in window_days.values() if level > 0)

    # Any window day GitHub didn't return data for is treated as empty too.
    all_window_dates = {WINDOW_START + timedelta(days=i) for i in range(total_days)}
    empty_days = sorted(
        day for day in all_window_dates
        if window_days.get(day, 0) == 0
    )

    fill_pct = (filled_days / total_days * 100) if total_days else 0.0
    needed_filled = math.ceil(TARGET_FILL_RATIO * total_days)
    to_fill = max(0, needed_filled - filled_days)
    to_fill = min(to_fill, len(empty_days))

    print(f"Username:             {username}")
    print(f"Window:               {WINDOW_START.isoformat()} .. {today.isoformat()}")
    print(f"Total days in window: {total_days}")
    print(f"Days with data found: {known_days}")
    print(f"Filled days:          {filled_days}")
    print(f"Current fill %:       {fill_pct:.1f}%")
    print(f"Target fill % (80%):  {needed_filled} days filled")
    print(f"Empty days available: {len(empty_days)}")
    print(f"Empty days to fill:   {to_fill}")

    OUTPUT_PATH.write_text(
        json.dumps(
            {
                "username": username,
                "window_start": WINDOW_START.isoformat(),
                "window_end": today.isoformat(),
                "generated_at": datetime.now().isoformat(timespec="seconds"),
                "total_days": total_days,
                "filled_days": filled_days,
                "fill_pct": round(fill_pct, 2),
                "needed": to_fill,
                "empty_days": [d.isoformat() for d in empty_days],
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"\nSaved {len(empty_days)} empty day(s) (needed={to_fill}) to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
