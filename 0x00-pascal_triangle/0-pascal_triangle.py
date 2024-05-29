#!/usr/bin/python3
"""
0-pascal_triangle.py
"""


def pascal_triangle(n):
    """
    A function that returns a list of lists of integers
    """
    if n <= 0:
        return []

    triangle = []
    # n = 3
    for i in range(n):
        row = [1] * (i + 1) # [1] * (3 + 1) = [1, 1, 1, 1]
        print (row)
        # range(2, 3)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j] 
                    # triangle[3 -1][2 - 1] + triangle[3 - 1][2]
                    # triangle[2][1] + triangle[2][2]
            # row[2] = 2 + 1 = 3
            print (3) 
        triangle.append(row)
        # i = 0: triangle = [[1]]
        # i = 1: triangle = [[1],[1, 1]]
        # i = 2: triangle = [[1], [1, 1], [1, 2, 1]]
        # i = 3: triangle = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
        

    print(triangle)


    return triangle
