#!/usr/bin/python3
""" pascal's triangle """


def pascal_triangle(n):
    """
    Generate a Pascal's triangle with n rows.

    Parameters:
    n (int): The number of rows for the Pascal's triangle.

    Returns:
    list: A list of lists representing the Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)  # Initialize row with ones
        for j in range(1, i):
            row[j] = (
                triangle[i - 1][j - 1] + triangle[i - 1][j]
            )  # Calculate values based on the previous row
        triangle.append(row)

    return triangle
