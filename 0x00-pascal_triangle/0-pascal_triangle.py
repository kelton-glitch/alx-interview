#!/usr/bin/python3
"""
0. Pascal's Triangle
"""

def pascal_triangle(n):
    """Create a function def pascal_triangle(n) : that returns a list of
    lists of integers representing the Pascal’s triangle of n.
    """
    res = []
    if n > 0:
        for i in range(n):
            row = [1]
            for j in range(i):
                row.append(row[j] + row[j + 1])
            res.append(row)
    return res
