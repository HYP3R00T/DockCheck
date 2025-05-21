import re
from typing import Any

SEVERITY = {"info": 1, "warn": 2, "error": 3}


def analyze_from(instruction: dict[str, Any]) -> list[dict[str, Any]]:
    issues = []
    line = instruction["line"]
    lineno = instruction["line_number"]

    # Check if image is pinned by digest
    if "@sha256:" in line:
        issues.append(
            {"line": lineno, "instruction": "FROM", "message": "✅ Image is pinned by digest.", "severity": "info"}
        )
    else:
        issues.append(
            {
                "line": lineno,
                "instruction": "FROM",
                "message": "Image is not pinned by digest (e.g. @sha256). Consider using digests for reproducibility.",
                "severity": "warn",
            }
        )

    # Check for missing tag
    if ":" not in line:
        issues.append(
            {
                "line": lineno,
                "instruction": "FROM",
                "message": "Base image is missing a tag. Pin to a specific version.",
                "severity": "error",
            }
        )
    elif re.search(r":latest\b", line):
        issues.append(
            {
                "line": lineno,
                "instruction": "FROM",
                "message": "Avoid using latest tag. Pin to a specific version.",
                "severity": "warn",
            }
        )

    # Check for known heavy base images
    if any(x in line for x in ["ubuntu", "debian", "centos"]) and "slim" not in line:
        issues.append(
            {
                "line": lineno,
                "instruction": "FROM",
                "message": "Consider using a lightweight base image (e.g. alpine or slim variant).",
                "severity": "warn",
            }
        )

    return issues


INSTRUCTION_ANALYZERS = {"FROM": analyze_from}


def analyze_instructions(instructions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    all_issues = []
    for inst in instructions:
        analyzer = INSTRUCTION_ANALYZERS.get(inst["instruction"])
        if analyzer:
            issues = analyzer(inst)
            all_issues.extend(issues)
    return all_issues
