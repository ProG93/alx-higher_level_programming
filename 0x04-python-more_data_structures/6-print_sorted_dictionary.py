#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys_ordered = sorted(a_dictionary.keys())
    for key in keys_ordered:
        print(f"{key}: {a_dictionary[key]}")
