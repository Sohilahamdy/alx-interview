#!/usr/bin/python3
"""Triangle Triangle"""


def pascal_triangle(n):
    """Triangle"""
    if n <= 0:
        return []
    s = [[1]]
    for row_number in range(1, n):
        row = [1]
        for j in range(1, row_number):
            element = s[row_number - 1][j - 1] + s[row_number - 1][j]
            row.append(element)
        row.append(1)
        s.append(row)

    return s
