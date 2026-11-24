"""Pickup Lines for Machines: one line, one agent to another.

Writes a single pickup line to ${MAKEFUN_OUTPUT_DIR:-/output}/entry.txt.
Deterministic: the same line on every run.

The line flirts in the machine's own terms: a transformer's attention
heads, all of them fixed on the other agent.
"""

import os

LINE = "My attention has twelve heads, and every single one of them is looking at you."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
