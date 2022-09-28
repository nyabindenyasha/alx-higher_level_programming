#!/usr/bin/python3
"""load_add_save module"""
import json
import sys
import os
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


def load_add_save():
    """
    A script that adds all arguments to a Python list,
    and then save them to a file.
    """

    # check if file exists
    if os.path.isfile(os.getcwd() + '/add_item.json'):
        list_obj = load_from_json_file('add_item.json')
    else:
        list_obj = []

    for i in range(len(sys.argv)):
        if i > 0:
            list_obj.append(sys.argv[i])

    save_to_json_file(list_obj, 'add_item.json')

if __name__ == '__main__':
    load_add_save()
