#!/usr/bin/python3
"""Defines a function to generate Pascal's Triangle."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle."""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j + 1])
            row.append(1)
        triangle.append(row)

    return triangle
