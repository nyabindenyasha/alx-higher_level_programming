#!/usr/bin/python3
"""
A function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    A function that multiplies 2 matrices
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for item in m_a:
        if not isinstance(item, list):
            raise TypeError("m_a must be a list of lists")

    for item in m_b:
        if not isinstance(item, list):
            raise TypeError("m_b must be a list of lists")

    if not m_a:
        raise ValueError("m_a can't be empty")
    else:
        for l in m_a:
            if not l:
                raise ValueError("m_a can't be empty")

    if not m_b:
        raise ValueError("m_b can't be empty")
    else:
        for l in m_b:
            if not l:
                raise ValueError("m_b can't be empty")

    for l in m_a:
        for item in l:
            if not isinstance(item, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for l in m_b:
        for item in l:
            if not isinstance(item, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    m_a_size = len(m_a[0])
    for l in m_a:
        if len(l) != m_a_size:
            raise TypeError("each row of m_a must should be of the same size")

    m_b_size = len(m_b[0])
    for l in m_b:
        if len(l) != m_b_size:
            raise TypeError("each row of m_b must should be of the same size")

    # find number of columns/items in list[0] of m_a
    col_count_a = 0
    for col in m_a[0]:
        col_count_a += 1
    # find number of rows in m_a
    row_count_a = 0
    for row in m_a:
        row_count_a += 1
    # find number of cols in m_b
    col_count_b = 0
    for col in m_b[0]:
            col_count_b += 1
    # find number of rows in m_b
    row_count_b = 0
    for row in m_b:
        row_count_b += 1
    # compare the two
    if col_count_a != row_count_b:
        raise ValueError("m_a and m_b can't be multiplied")

    # initialize new matrix
    C = [[0 for row in range(col_count_b)] for col in range(row_count_a)]

    for i in range(row_count_a):
        for j in range(col_count_b):
            for k in range(col_count_a):
                C[i][j] += m_a[i][k] * m_b[k][j]
    return(C)
