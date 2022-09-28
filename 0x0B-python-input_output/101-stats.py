#!/usr/bin/python3
"""append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file,
    after each line containing a specific string
    """

    ret_list = []
    with open(filename, mode='r', encoding="utf-8") as f:
        full_file = f.read()
        file_list = full_file.split('\n')
        for line in file_list:
            ret_list.append(line + '\n')
            if search_string in line:
                ret_list.append(new_string)

    with open(filename, mode='w', encoding="utf-8") as f:
        ret_string = "".join(ret_list)
        f.write(ret_string)
