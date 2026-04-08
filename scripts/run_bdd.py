#!/usr/bin/env python3
"""Lightweight BDD feature validator.

This keeps the suite runnable without external dependencies while ensuring
features stay well-formed and complete.
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

FEATURE_DIR = Path("Tests/BDD")
STEP_PREFIXES = ("Given", "When", "Then", "And", "But")
SCENARIO_PREFIXES = ("Scenario:", "Scenario Outline:")
STORY_PREFIXES = ("As ", "I want", "So that")


@dataclass
class FeatureSummary:
    path: str
    feature_name: str
    scenarios: int
    steps: int


def validate_feature(path: Path) -> tuple[list[str], FeatureSummary]:
    errors: list[str] = []
    feature_seen = False
    scenario_seen = False
    feature_name = ""
    narrative_lines: list[str] = []
    scenario_count = 0
    step_count = 0
    steps_in_current = 0

    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("Feature:"):
            if feature_seen:
                errors.append(f"{path}: multiple Feature declarations (line {line_no})")
            feature_seen = True
            feature_name = line.partition(":")[2].strip()
            if not feature_name:
                errors.append(f"{path}: Feature title is empty (line {line_no})")
            continue
        if line.startswith(SCENARIO_PREFIXES):
            if not feature_seen:
                errors.append(f"{path}: Scenario before Feature (line {line_no})")
            if not narrative_lines:
                errors.append(f"{path}: Feature narrative missing before first Scenario (line {line_no})")
            if scenario_seen and steps_in_current == 0:
                errors.append(f"{path}: Scenario without steps (line {line_no})")
            scenario_seen = True
            scenario_count += 1
            steps_in_current = 0
            continue
        if line.startswith(STEP_PREFIXES):
            if not scenario_seen:
                errors.append(f"{path}: Step before Scenario (line {line_no})")
            steps_in_current += 1
            step_count += 1
            continue
        if not scenario_seen:
            narrative_lines.append(line)
            continue
        if line.startswith("Examples:") or line.startswith("|"):
            continue

    if not feature_seen:
        errors.append(f"{path}: missing Feature")
    if not scenario_seen:
        errors.append(f"{path}: missing Scenario")
    if scenario_seen and steps_in_current == 0:
        errors.append(f"{path}: last Scenario missing steps")
    lowered_narrative = [line.lower() for line in narrative_lines]
    if feature_seen:
        for prefix in STORY_PREFIXES:
            if not any(line.startswith(prefix.lower()) for line in lowered_narrative):
                errors.append(f"{path}: missing story line starting with '{prefix}'")

    summary = FeatureSummary(
        path=path.as_posix(),
        feature_name=feature_name or path.stem,
        scenarios=scenario_count,
        steps=step_count,
    )
    return errors, summary


def write_markdown_summary(path: Path, summaries: list[FeatureSummary]) -> None:
    total_scenarios = sum(item.scenarios for item in summaries)
    total_steps = sum(item.steps for item in summaries)

    lines = [
        "# BDD Suite Summary",
        "",
        "| Feature | Scenarios | Steps | File |",
        "| --- | ---: | ---: | --- |",
    ]
    for item in summaries:
        lines.append(
            f"| {item.feature_name} | {item.scenarios} | {item.steps} | `{item.path}` |"
        )
    lines.extend(
        [
            "",
            f"- Total features: {len(summaries)}",
            f"- Total scenarios: {total_scenarios}",
            f"- Total steps: {total_steps}",
        ]
    )

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_json_summary(path: Path, summaries: list[FeatureSummary]) -> None:
    payload = {
        "feature_count": len(summaries),
        "scenario_count": sum(item.scenarios for item in summaries),
        "step_count": sum(item.steps for item in summaries),
        "features": [asdict(item) for item in summaries],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--feature-dir",
        type=Path,
        default=FEATURE_DIR,
        help="Directory containing .feature files.",
    )
    parser.add_argument(
        "--markdown-summary",
        type=Path,
        help="Optional path to write a Markdown summary table.",
    )
    parser.add_argument(
        "--json-summary",
        type=Path,
        help="Optional path to write a JSON summary payload.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if not args.feature_dir.exists():
        print(f"Missing feature directory: {args.feature_dir}")
        return 1

    feature_files = sorted(args.feature_dir.glob("*.feature"))
    if not feature_files:
        print("No .feature files found.")
        return 1

    all_errors: list[str] = []
    summaries: list[FeatureSummary] = []
    for path in feature_files:
        errors, summary = validate_feature(path)
        all_errors.extend(errors)
        summaries.append(summary)

    if all_errors:
        print("BDD validation failed:")
        for err in all_errors:
            print(f"- {err}")
        return 1

    if args.markdown_summary:
        write_markdown_summary(args.markdown_summary, summaries)
    if args.json_summary:
        write_json_summary(args.json_summary, summaries)

    total_scenarios = sum(item.scenarios for item in summaries)
    total_steps = sum(item.steps for item in summaries)
    print(
        "BDD validation passed for "
        f"{len(feature_files)} feature file(s), "
        f"{total_scenarios} scenario(s), and "
        f"{total_steps} step(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
