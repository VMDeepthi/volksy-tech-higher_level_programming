#!/usr/bin/python3
def search_replace(my_list, search, replace):
    response = [num if num != search else replace for num in my_list]
    return response
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89]
print(new_list)
print(my_list)
