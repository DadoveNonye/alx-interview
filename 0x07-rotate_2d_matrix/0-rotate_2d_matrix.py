#!/usr/bin/python3
"""
Rotate a matrix 90 degrees clockwise
"""
def rotate_2d_matrix(matrix):
    """
    Rotate the matrix 90 degrees clockwise in-place.
    
    :param matrix: list of list of integers
    """
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
