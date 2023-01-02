#!/usr/bin/python3
def fizbuzz():
    for a in range(51):
        if a % 5 == 0 and a % 3 == 0:
            print("Fizzbuzz", end=" ")
            continue
        elif a % 5 == 0:
             print("Buzz", end=" ")
             continue
        elif a % 3 == 0:
        print("Fizz", end=" "))
        continue
        print(a, end=" ")
