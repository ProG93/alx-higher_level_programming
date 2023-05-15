#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mat in matrix:
        for rix in mat:
            if rix == mat[-1]:
                print("{:d}".format(rix), end='')
            else:
                print("{:d}".format(rix), end='')
            print('')
