#!/usr/bin/python3
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    filename = "add_item.json"
    arg_ls = sys.argv
    try:
        ls = load_from_json_file(filename)
    except FileNotFoundError:
        save_to_json_file(arg_ls[1:], filename)

    ls += arg_ls[1:]
    save_to_json_file(ls, filename)
