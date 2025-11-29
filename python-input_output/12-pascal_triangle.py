#!/usr/bin/python3
"""Module that returns Pascal's triangle of size n."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        prev_row = triangle[i - 1]
        row = [1]  # First element is always 1
        # Compute middle elements as sum of two elements above
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle
