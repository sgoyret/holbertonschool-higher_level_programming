#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    sorted_list = list(a_dictionary.keys())
    sorted_list.sort()
    for key in sorted_list:
        print("{}: {}".format(i, a_dictionary.get(i)))
