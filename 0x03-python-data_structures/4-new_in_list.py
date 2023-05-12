#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    item = len(my_list) - 1

    if item < 0 and idx > item:
        return my_list
    new_list = my_list.copy()
    new_list[idx] = element
    return new_element
