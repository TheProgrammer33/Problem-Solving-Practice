import math

"""
The objective is to write a function that finds the sum of all positive multiples of 3 or 5 below n.
"""
def sumMults(num):
    total = 0
    for i in range(3, num):
        if (i % 3 == 0 or i % 5 == 0):
            total += i
    return total

# https://www.freecodecamp.org/learn/coding-interview-prep/rosetta-code/sum-multiples-of-3-and-5