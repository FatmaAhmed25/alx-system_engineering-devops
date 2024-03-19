#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and len(matrix[0]) == 0:
        print("")
    else:
        for x in matrix:
            for y in x:
                if y != x[-1]:
                    print("{:d}".format(y), end=" ")
                else:
                    print("{:d}".format(y))
