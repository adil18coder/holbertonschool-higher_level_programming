#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for row in matrix:
        output_row = ""
        if not row:
            print()
            continue
        for i in range(len(row)):
            formatted_int = "{:d}".format(row[i])
            output_row += formatted_int
            if i < len(row) - 1:
                output_row += " "
        print(output_row)
