#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        pass
    else:
        row = 0
        while row < len(matrix):
            column = 0
            while column < len(matrix[row]):
                print("{:d}".format(matrix[row][column]), end="")
                column += 1
                if column != 3:
                    print(" ", end="")
                else:
                    print()
            row += 1
