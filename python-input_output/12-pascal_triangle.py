#!/usr/bin/python3
"""pascal triangle
"""


def pascal_triangle(n):
    """ makes a list of lists representing a pascal tringle """
    lista = []
    if n <= 0:
        return lista
    if n >= 1:
        lista.append([1])
    for i in range(1, n):
        lista.append([1])
        for j in range(len(lista[i - 1]) - 1):
            lista[i].append(lista[i - 1][j] + lista[i - 1][j + 1])
        lista[i].append(1)
    return lista
