import json
from typing import Generator


def format_report(
    entries: Generator[dict, None, None],
    fmt: str = "text"
) -> str:

    results = list(entries)

    if not results:
        return "No log entries found matching the given filters."

    if fmt == "json":
        serializable = [
            {**e, "timestamp": e["timestamp"].isoformat()}
            for e in results
        ]
        return json.dumps(serializable, indent=2)

    lines = []

    for e in results:
        ts = e["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
        lines.append(f"[{e['level']}] {ts} — {e['message']}")

    summary = f"\n--- {len(results)} entries found ---"

    return "\n".join(lines) + summary