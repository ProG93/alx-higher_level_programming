#!/usr/bin/python3
def no_c(my_string):
    no_c_string = my_string.translate({ord(i): None for i in 'Cc'})
    return no_c_string
