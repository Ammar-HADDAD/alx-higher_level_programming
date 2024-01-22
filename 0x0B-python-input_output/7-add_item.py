#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file
"""

from sys import argv
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing list from file or create an empty list
json_list = load_from_json_file(filename) if path.exists(filename) else []

# Add command line arguments to the list
json_list.extend(argv[1:])

# Save the updated list to the file
save_to_json_file(json_list, filename)
