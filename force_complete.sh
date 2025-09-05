#!/bin/bash
set -euo pipefail

echo "=== Starting forced completion approach ==="

# Run cursor-agent in background
cursor-agent -p "You are updating documentation summary files. 

TASK: Check if docs/$CHANGED_SUBDIRS/llms.txt and docs/$CHANGED_SUBDIRS/llms-full.txt need updates based on PR 296.

PROCESS:
1. Get diff: gh pr diff 296
2. Read docs/$CHANGED_SUBDIRS/llms.txt 
3. Read docs/$CHANGED_SUBDIRS/llms-full.txt
4. If changes warrant updates: modify the files
5. If no updates needed: do nothing
6. Print 'ANALYSIS_COMPLETE' and stop

CRITICAL: You have 5 minutes to complete this. Print 'ANALYSIS_COMPLETE' when done and exit immediately. Do not commit or push." \
--force --model "$MODEL" --output-format=text &

AGENT_PID=$!
echo "Started cursor-agent with PID: $AGENT_PID"

# Force kill after 5 minutes
(sleep 300; echo "=== Forcing completion after 5 minutes ==="; kill -9 $AGENT_PID 2>/dev/null) &
KILLER_PID=$!

# Wait for completion
if wait $AGENT_PID 2>/dev/null; then
  echo "=== Agent completed normally ==="
  kill $KILLER_PID 2>/dev/null || true
else
  echo "=== Agent was terminated ==="
fi

echo "=== Process finished ==="
