#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    new = a_dictionary.copy()

    for key in new.keys():
        new[key] = new[key] * 2

    return new
