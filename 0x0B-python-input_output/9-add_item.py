#!/usr/bin/python3
import sys
from os.path import exists


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
if not exists(filename):
    open(filename, "w", encoding="utf-8")

saved_list = load_from_json_file(filename)
to_save_list = []

if saved_list is not None:
    for e in saved_list:
        to_save_list.append(e)

for i in range(1, len(sys.argv)):
    to_save_list.append(sys.argv[i])

save_to_json_file(to_save_list, filename)
