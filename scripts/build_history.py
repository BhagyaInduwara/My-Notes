#!/usr/bin/env python3
"""
Build a backdated commit history that copies source_notes/ into notes/,
one small chunk at a time, spread across the empty days listed in
scripts/empty_days.json, so the GitHub contribution graph fills in.

Usage:
    python scripts/build_history.py --dry-run
    python scripts/build_history.py
"""

import argparse
import json
import math
import random
import subprocess
import sys
from datetime import datetime, time, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = REPO_ROOT / "source_notes"
NOTES_DIR = REPO_ROOT / "notes"
PROGRESS_PATH = REPO_ROOT / "PROGRESS.md"
EMPTY_DAYS_PATH = Path(__file__).resolve().parent / "empty_days.json"

DAY_START = time(8, 0)
DAY_END = time(23, 0)
MIN_COMMITS_PER_DAY = 1
MAX_COMMITS_PER_DAY = 4

# (source filename, notes filename, topic label used in commit messages)
TOPIC_ORDER = [
    ("01_html_basics.md", "01_html_basics.md", "HTML"),
    ("02_css_basics.md", "02_css_basics.md", "CSS"),
    ("03_javascript_basics.md", "03_javascript_basics.md", "JavaScript"),
    ("04_python_basics.md", "04_python_basics.md", "Python"),
    ("05_oop_basics.md", "05_oop_basics.md", "OOP"),
    ("06_sql_basics.md", "06_sql_basics.md", "SQL"),
    ("07_git_basics.md", "07_git_basics.md", "Git"),
    ("08_dsa_basics.md", "08_dsa_basics.md", "Data Structures & Algorithms"),
]


def split_into_chunks(text: str):
    """Split markdown text on blank lines, never inside a ``` fence."""
    lines = text.split("\n")
    chunks = []
    current = []
    in_fence = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            current.append(line)
            continue

        if stripped == "" and not in_fence:
            if current:
                chunk = "\n".join(current).strip("\n")
                if chunk.strip():
                    chunks.append(chunk)
                current = []
            continue

        current.append(line)

    if current:
        chunk = "\n".join(current).strip("\n")
        if chunk.strip():
            chunks.append(chunk)

    return _merge_pure_code_chunks(chunks)


def _is_pure_code_chunk(chunk: str) -> bool:
    lines = [ln for ln in chunk.splitlines() if ln.strip() != ""]
    return bool(lines) and lines[0].strip().startswith("```") and lines[-1].strip().startswith("```")


def _merge_pure_code_chunks(chunks):
    """Fold a chunk that is *only* a code fence into the previous chunk,
    so explanations stay paired with their example in one commit."""
    merged = []
    for chunk in chunks:
        if merged and _is_pure_code_chunk(chunk):
            merged[-1] = merged[-1] + "\n\n" + chunk
        else:
            merged.append(chunk)
    return merged


def _truncate_at_word(text: str, limit: int = 50) -> str:
    text = text.strip().lstrip("-*").strip()
    if len(text) <= limit:
        return text.rstrip(".:,")
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut.rstrip(".:,") + "..."


def chunk_label(chunk: str) -> str:
    """Derive a short descriptive label from a chunk's first heading/line."""
    for line in chunk.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip()
        if stripped:
            return _truncate_at_word(stripped)
    return "notes"


def build_chunk_queue():
    """Return an ordered list of (topic_label, notes_filename, chunk_text)."""
    queue = []
    for source_name, notes_name, topic_label in TOPIC_ORDER:
        source_path = SOURCE_DIR / source_name
        if not source_path.exists():
            raise SystemExit(f"Missing source file: {source_path}")
        text = source_path.read_text(encoding="utf-8")
        for chunk in split_into_chunks(text):
            queue.append((topic_label, notes_name, chunk))
    return queue


def load_empty_days():
    if not EMPTY_DAYS_PATH.exists():
        raise SystemExit(
            f"{EMPTY_DAYS_PATH} not found. Run scripts/check_graph.py first."
        )
    data = json.loads(EMPTY_DAYS_PATH.read_text(encoding="utf-8"))
    all_empty = [datetime.strptime(d, "%Y-%m-%d").date() for d in data["empty_days"]]
    needed = data["needed"]
    if needed > len(all_empty):
        raise SystemExit("`needed` exceeds available empty days in empty_days.json.")
    selected = random.sample(all_empty, needed)
    selected.sort()
    return selected


def random_times_for_day(day, count, now):
    """Return `count` sorted datetimes for `day`, all in [08:00, 23:00] and never in the future."""
    start_dt = datetime.combine(day, DAY_START)
    end_dt = datetime.combine(day, DAY_END)

    if day == now.date():
        end_dt = min(end_dt, now - timedelta(minutes=1))
        if end_dt <= start_dt:
            # Too early in the day for the normal window; use whatever time is left before now.
            start_dt = datetime.combine(day, time(0, 1))
            end_dt = now - timedelta(minutes=1)

    span_seconds = max(int((end_dt - start_dt).total_seconds()), 1)
    offsets = sorted(random.randint(0, span_seconds) for _ in range(count))
    return [start_dt + timedelta(seconds=off) for off in offsets]


def build_plan(selected_days, chunk_queue, now):
    """
    Assign chunks and PROGRESS filler entries to each selected day.
    Returns a list of day-plans: {date, commits: [ (kind, payload, message) ]}
    """
    plan = []
    chunks = list(chunk_queue)
    chunk_i = 0
    n_chunks = len(chunks)
    n_days = len(selected_days)
    filler_topics = [label for _, _, label in TOPIC_ORDER]
    filler_i = 0

    for day_idx, day in enumerate(selected_days):
        remaining_days = n_days - day_idx
        remaining_chunks = n_chunks - chunk_i
        commits = []

        if remaining_chunks <= 0:
            take = 0
        else:
            # Pace consumption so chunks last across the *whole* remaining
            # date range instead of running out early and leaving a long
            # filler-only tail.
            avg = remaining_chunks / remaining_days
            low = max(MIN_COMMITS_PER_DAY, min(MAX_COMMITS_PER_DAY, math.floor(avg)))
            high = max(low, min(MAX_COMMITS_PER_DAY, math.ceil(avg) + 1))
            take = min(random.randint(low, high), remaining_chunks)

        for _ in range(take):
            topic_label, notes_name, chunk_text = chunks[chunk_i]
            chunk_i += 1
            label = chunk_label(chunk_text)
            message = f"Add {topic_label} notes: {label}"
            commits.append(("chunk", (notes_name, chunk_text), message))

        if not commits:
            topic = filler_topics[filler_i % len(filler_topics)]
            filler_i += 1
            message = f"Revised: {topic}"
            commits.append(("progress", topic, message))

        plan.append({"date": day, "commits": commits})

    remaining_chunks = n_chunks - chunk_i
    return plan, remaining_chunks


def run_git_commit(files_changed, message, when: datetime, dry_run: bool):
    date_str = when.astimezone().strftime("%Y-%m-%d %H:%M:%S %z")
    if dry_run:
        return

    subprocess.run(["git", "add", *files_changed], cwd=REPO_ROOT, check=True)
    env = {
        "GIT_AUTHOR_DATE": date_str,
        "GIT_COMMITTER_DATE": date_str,
    }
    import os

    full_env = os.environ.copy()
    full_env.update(env)
    subprocess.run(
        ["git", "commit", "-m", message],
        cwd=REPO_ROOT,
        check=True,
        env=full_env,
    )


def apply_chunk_commit(notes_name, chunk_text):
    NOTES_DIR.mkdir(exist_ok=True)
    notes_path = NOTES_DIR / notes_name
    existing = notes_path.read_text(encoding="utf-8") if notes_path.exists() else ""
    if existing and not existing.endswith("\n\n"):
        existing = existing.rstrip("\n") + "\n\n"
    notes_path.write_text(existing + chunk_text.strip("\n") + "\n", encoding="utf-8")
    return [str(notes_path.relative_to(REPO_ROOT))]


def apply_progress_commit(topic, when: datetime):
    existing = PROGRESS_PATH.read_text(encoding="utf-8") if PROGRESS_PATH.exists() else "# Learning Log\n"
    line = f"- {when.date().isoformat()}: Revised: {topic}\n"
    if not existing.endswith("\n"):
        existing += "\n"
    PROGRESS_PATH.write_text(existing + line, encoding="utf-8")
    return [str(PROGRESS_PATH.relative_to(REPO_ROOT))]


def apply_setup_commit():
    files = []
    for name in ("README.md", "PROGRESS.md", ".gitignore", "LICENSE"):
        path = REPO_ROOT / name
        if path.exists():
            files.append(str(path.relative_to(REPO_ROOT)))
    for name in ("check_graph.py", "build_history.py"):
        path = REPO_ROOT / "scripts" / name
        files.append(str(path.relative_to(REPO_ROOT)))
    return files


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    now = datetime.now()
    selected_days = load_empty_days()
    if not selected_days:
        print("No empty days need filling. Nothing to do.")
        return

    chunk_queue = build_chunk_queue()
    plan, remaining_chunks = build_plan(selected_days, chunk_queue, now)

    total_commits = sum(len(day["commits"]) for day in plan) + 1  # +1 for setup commit
    chunk_commits = sum(
        1 for day in plan for kind, *_ in day["commits"] if kind == "chunk"
    ) + 1  # setup commit counts as "real content"
    filler_commits = total_commits - chunk_commits

    print(f"Days to fill:        {len(plan)}")
    print(f"Total chunks found:  {len(chunk_queue)}")
    print(f"Chunks used:         {len(chunk_queue) - remaining_chunks}")
    print(f"Chunks left over:    {remaining_chunks}")
    print(f"Total commits:       {total_commits}")
    print(f"  content commits:   {chunk_commits}")
    print(f"  filler commits:    {filler_commits}")

    if remaining_chunks == 0 and filler_commits > chunk_commits:
        print(
            "\nWARNING: more filler (PROGRESS.md) commits than content commits.\n"
            "Consider expanding source_notes/ before running for real.",
            file=sys.stderr,
        )

    # Build one flat, time-ordered schedule shared by both dry-run and real
    # run, so the preview can never drift from what actually gets committed.
    schedule = []
    setup_message = "Add README, license, and project scaffolding"
    for day_idx, day_plan in enumerate(plan):
        day = day_plan["date"]
        commits = day_plan["commits"]
        extra = 1 if day_idx == 0 else 0  # first day also carries the setup commit
        times = random_times_for_day(day, len(commits) + extra, now)
        if extra:
            schedule.append((times[0], "setup", None, setup_message))
            times = times[1:]
        for when, (kind, payload, message) in zip(times, commits):
            schedule.append((when, kind, payload, message))

    if args.dry_run:
        print("\n--- DRY RUN: planned commits ---")
        for when, kind, payload, message in schedule:
            print(f"{when}  [{kind:>8}]  {message}")
        print(f"\nFirst commit day: {plan[0]['date']}")
        print(f"Last commit day:  {plan[-1]['date']}")
        return

    # --- Real run ---
    for when, kind, payload, message in schedule:
        if kind == "setup":
            files = apply_setup_commit()
        elif kind == "chunk":
            notes_name, chunk_text = payload
            files = apply_chunk_commit(notes_name, chunk_text)
        else:
            files = apply_progress_commit(payload, when)
        run_git_commit(files, message, when, dry_run=False)
        print(f"[commit] {when}  {message}")

    print(f"\nDone. First commit day: {plan[0]['date']}. Last commit day: {plan[-1]['date']}.")


if __name__ == "__main__":
    main()
