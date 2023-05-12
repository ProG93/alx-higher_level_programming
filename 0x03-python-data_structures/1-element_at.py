#!/usr/bin/python3
def element_at(my_list, idx):
    item = len(my_list) - 1

    if idx < 1 or idx > item:
        return None
    else:
        return my_list[idx]
