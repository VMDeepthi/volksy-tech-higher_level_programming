#!/usr/bin/python3

"""
Multiplies 2 matrices by using 'numpy' module.
"""
import numpy as lazy


def lazy_matrix_mul(m_a, m_b):
    """
    Function to multiplies 2 matrices
    """
    return lazy.matmul(m_a, m_b)
