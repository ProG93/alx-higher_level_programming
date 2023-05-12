#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    item = len(my_list) - 1

    if item < 0 and idx > item:
        return my_list
    else:
        my_list[idx] = element
        return my_list
