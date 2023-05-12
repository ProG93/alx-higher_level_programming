#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mat in range(len(matrix)):
        for rix in range(len(mat)):
            if rix != 0:
                print(" ", end='')
            print("{:d}".format(matrix[mat][rix]), end='')
            print()
