#!/usr/bin/env python3
import json, sys
from pathlib import Path
ORDER = {"in_progress": 0, "in_review": 1, "todo": 2}

def main(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    tickets = data.get("tickets") or []
    open_ones = [t for t in tickets if t.get("status") in ORDER]
    if not open_ones:
        print("idle"); return 2
    open_ones.sort(key=lambda t: (ORDER[t["status"]], int(t.get("priority") or 9), t.get("id") or ""))
    print(json.dumps(open_ones[0], indent=2)); return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "board.json"))
