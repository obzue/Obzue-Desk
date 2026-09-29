#!/usr/bin/env python3
import json, sys
from pathlib import Path
STATUSES = {"todo", "in_progress", "in_review", "done", "blocked"}
WEAK = ("looks good", "seems fine", "i think")

def main(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    tickets = data.get("tickets") or []
    if not tickets:
        print("no tickets"); return 1
    for t in tickets:
        for key in ("id", "title", "status", "owner", "priority", "probe"):
            if not str(t.get(key, "")).strip():
                print(f"{t.get('id')} missing {key}"); return 1
        if t["status"] not in STATUSES:
            print(f"{t['id']} bad status"); return 1
        if any(w in str(t["probe"]).lower() for w in WEAK):
            print(f"{t['id']} probe is a self-grade"); return 1
    print(f"ok {len(tickets)} tickets"); return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "board.json"))
