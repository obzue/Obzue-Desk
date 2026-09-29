#!/usr/bin/env python3
import sys
from pathlib import Path
ALLOWED = {"pass", "fail", "blocked"}
BANNED = ("i think", "looks good", "seems fine", "probably done")

def main(path):
    p = Path(path)
    if not p.exists():
        print(f"missing {path}"); return 1
    lines = [ln.strip() for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip() and not ln.startswith("#")]
    if not lines:
        print("empty trail"); return 1
    for i, line in enumerate(lines, 1):
        parts = [part.strip() for part in line.split("|")]
        if len(parts) != 4:
            print(f"line {i}: need four fields"); return 1
        intent, limit, evidence, result = parts
        if not all((intent, limit, evidence, result)):
            print(f"line {i}: empty field"); return 1
        if result.lower() not in ALLOWED:
            print(f"line {i}: result must be pass|fail|blocked"); return 1
        if any(b in f"{evidence} {result}".lower() for b in BANNED):
            print(f"line {i}: evidence looks like a self-grade"); return 1
    print(f"ok {len(lines)} rows"); return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "trail.txt"))
