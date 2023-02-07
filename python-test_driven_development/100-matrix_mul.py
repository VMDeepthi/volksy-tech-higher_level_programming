#!/usr/bin/python3
"""
    Write a function that mul
"""


def transpose(matrix):
    """ transpose a matrix """
    new_matrix = []
    for column in matrix[0]:
        new_matrix.append([])
    for row in matrix:
        for index, item in enumerate(row):
            new_matrix[index].append(item)
    return new_matrix


def dot_product(row_a, row_b):
    """ multiply dot 2 matrix """
    sum = 0
    for index, item in enumerate(row_a):
        sum += item * row_b[index]
    return sum


def mult(m_a, m_b):
    """ multiply a matrix """
    t_b = transpose(m_b)
    new_matrix = []
    for row in m_a:
        new_matrix.append([])
    result = 0
    for index_a, row_a in enumerate(m_a):
        for index_b, row_b in enumerate(t_b):
            result = dot_product(row_a, row_b)
            new_matrix[index_a].append(result)
    return new_matrix


def matrix_mul(m_a, m_b):
    """ matrix produc """
    a_list_error = "m_a must be a list"
    b_list_error = "m_b must be a list"
    a_list_list_error = "m_a must be a list of lists"
    b_list_list_error = "m_b must be a list of lists"
    a_empty_error = "m_a can't be empty"
    b_empty_error = "m_b can't be empty"
    a_int_error = "m_a should contain only integers or floats"
    b_int_error = "m_b should contain only integers or floats"
    a_rect_error = "each row of m_a must be of the same size"
    b_rect_error = "each row of m_b must be of the same size"
    cant_mult_error = "m_a and m_b can't be multiplied"
    if type(m_a) is not list:
        raise TypeError(a_list_error)
    if type(m_b) is not list:
        raise TypeError(b_list_error)
    for row in m_a:
        if type(row) is not list:
            raise TypeError(a_list_list_error)
    for row in m_b:
        if type(row) is not list:
            raise TypeError(b_list_list_error)
    if m_a == []:
        raise ValueError(a_empty_error)
    if m_b == []:
        raise ValueError(b_empty_error)
    for row in m_a:
        if row == []:
            raise ValueError(a_empty_error)
    for row in m_b:
        if row == []:
            raise ValueError(b_empty_error)
    longitud_a = len(m_a[0])
    longitud_b = len(m_b[0])
    for row in m_a:
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError(a_int_error)
    for row in m_b:
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError(b_int_error)
    for row in m_a:
        if len(row) != longitud_a:
            raise TypeError(a_rect_error)
    for row in m_b:
        if len(row) != longitud_b:
            raise TypeError(b_rect_error)
    if longitud_a != len(m_b):
        raise ValueError(cant_mult_error)
    return mult(m_a, m_b)
