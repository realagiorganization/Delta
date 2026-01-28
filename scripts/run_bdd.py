#!/usr/bin/env python3
"""Lightweight BDD feature validator.

This keeps the suite runnable without external dependencies while ensuring
features stay well-formed and complete.
"""
from __future__ import annotations

import sys
from pathlib import Path

FEATURE_DIR = Path("Tests/BDD")
STEP_PREFIXES = ("Given", "When", "Then", "And", "But")
SCENARIO_PREFIXES = ("Scenario:", "Scenario Outline:")


def validate_feature(path: Path) -> list[str]:
    errors: list[str] = []
    feature_seen = False
    scenario_seen = False
    steps_in_current = 0

    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("Feature:"):
            if feature_seen:
                errors.append(f"{path}: multiple Feature declarations (line {line_no})")
            feature_seen = True
            continue
        if line.startswith(SCENARIO_PREFIXES):
            if not feature_seen:
                errors.append(f"{path}: Scenario before Feature (line {line_no})")
            if scenario_seen and steps_in_current == 0:
                errors.append(f"{path}: Scenario without steps (line {line_no})")
            scenario_seen = True
            steps_in_current = 0
            continue
        if line.startswith(STEP_PREFIXES):
            if not scenario_seen:
                errors.append(f"{path}: Step before Scenario (line {line_no})")
            steps_in_current += 1
            continue

    if not feature_seen:
        errors.append(f"{path}: missing Feature")
    if not scenario_seen:
        errors.append(f"{path}: missing Scenario")
    if scenario_seen and steps_in_current == 0:
        errors.append(f"{path}: last Scenario missing steps")

    return errors


def main() -> int:
    if not FEATURE_DIR.exists():
        print(f"Missing feature directory: {FEATURE_DIR}")
        return 1

    feature_files = sorted(FEATURE_DIR.glob("*.feature"))
    if not feature_files:
        print("No .feature files found.")
        return 1

    all_errors: list[str] = []
    for path in feature_files:
        all_errors.extend(validate_feature(path))

    if all_errors:
        print("BDD validation failed:")
        for err in all_errors:
            print(f"- {err}")
        return 1

    print(f"BDD validation passed for {len(feature_files)} feature file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
