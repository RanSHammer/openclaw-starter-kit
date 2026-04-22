#!/usr/bin/env bash
# Watch Granola's cache file and re-export on any change.
CACHE_DIR="$HOME/Library/Application Support/Granola"
CACHE_FILE="$CACHE_DIR/cache-v6.json"
EXPORT_SCRIPT="$HOME/.openclaw/workspace/scripts/granola-sync/export.py"
LOG="$HOME/.openclaw/workspace/scripts/granola-sync/watch.log"

mkdir -p "$(dirname "$LOG")"
echo "[$(date)] Granola watcher starting" >> "$LOG"

# Do one export immediately in case there are pending notes
python3 "$EXPORT_SCRIPT" >> "$LOG" 2>&1

# Watch the cache file and re-export on changes (debounced)
fswatch -l 2 "$CACHE_FILE" | while read -r line; do
  echo "[$(date)] Change detected" >> "$LOG"
  python3 "$EXPORT_SCRIPT" >> "$LOG" 2>&1
done
