# Pythagorean Numbers Revisited
"""This program takes one positive int argument n and returns a list with Pythagorean Triples"""

import math

def compute_Pythagoreans(n):
    '''Returns List of Tuples'''
    if n > 0 and type(n) == int:
        return [(a, b, c) for a in range(3, n+1) for b in range(4, n+1) for c in range(5,n+1) if a**2+b**2==c**2]
    else:
        return []

n = int(input("Enter a number greater than zero: "))
print(compute_Pythagoreans(n))
