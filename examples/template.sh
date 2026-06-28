#!/bin/sh
source .venv/bin/activate

# Auto-increment the trial ID
FILE="./examples/trial_auto_id.txt"

if [ -f "$FILE" ]; then
    trial_id=$(cat "$FILE")
else
    trial_id=0
fi
trial_id=$((trial_id + 1))
echo "$trial_id" > "$FILE"

hermes-cli -o ./data --config_file ./examples/template.yml --experiment project=Template trial=$trial_d
