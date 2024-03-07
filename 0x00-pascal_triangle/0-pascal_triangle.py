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
        for i in range(1, n + 1):
            row = []
            level = 1
            for j in range(1, i + 1):
                row.append(level)
                level = level * (i - j) // j
            res.append(row)
    return res
