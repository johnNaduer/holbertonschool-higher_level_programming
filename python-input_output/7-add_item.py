#!/usr/bin/python3
"""script that adds all arguments to a Python list""" 
import sys
import json


filename = "add_item.json"

# Create a list to store all items
items = []

# Loop through all arguments and add them to the list
i = 1
while i < len(sys.argv):
    items.append(sys.argv[i])
    i = i + 1

# Write the list to the file
def save_to_json_file(my_obj, filename):
    """Function that writes an object to a text file."""
    new_json = json.dumps(my_obj)
    with open(filename, 'w') as file:
        file.write(new_json)

save_to_json_file(items, filename)

def load_from_json_file(filename):
    """Open the file specified by "filename" in read mode."""
    with open(filename, 'r') as file:
        read_file = file.read()
        new_data = json.loads(read_file)
        return (new_data)
