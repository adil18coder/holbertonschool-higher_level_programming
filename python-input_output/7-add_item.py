#!/usr/bin/python3
"""Script that adds all command-line arguments to a Python list
and saves them to a JSON file.
"""

import sys
from pathlib import Path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing list if file exists, else start with empty list
if Path(filename).exists():
    items = load_from_json_file(filename)
else:
    items = []

# Add all command-line arguments (excluding script name)
items.extend(sys.argv[1:])

# Save updated list back to JSON file
save_to_json_file(items, filename)
