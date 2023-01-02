#!/usr/bin/python3
for i in range(97, 123):
    a = chr(i)
    if a not in 'eq':
       print("{}" .format(a), end="")
