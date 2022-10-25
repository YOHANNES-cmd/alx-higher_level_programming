#!/usr/bin/python3
"""The to json string module"""
import json
from sys import argv
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


lp = []
if exists("add_item.json"):
    with open("add_item.json", "r", encoding="Utf-8") as file:
        lines = file.readlines()
        for i in lines:
            if i != "":
                lp = json.loads(i)
else:
    with open("add_item.json", "w", encoding="Utf-8") as file:
        pass

with open("add_item.json", "r", encoding="Utf-8") as file:
    lines = file.readlines()
    for i in lines:
        if i != "":
            lp = json.loads(i)

for i in range(1, len(argv)):
    lp.append(argv[i])

with open("add_item.json", "w", encoding="Utf-8") as file:
    lpo = "[" + ", ".join(lp) + "]"
    file.write(json.dumps(lp))
