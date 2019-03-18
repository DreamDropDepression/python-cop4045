"""
Pythagorean Triples
taken from http://mathforum.org/library/drmath/view/55811.html
"""

k = input("Enter max number K: ")
for m in range(2, k):
    for n in range(1, m):
        for d in range(1, k):
            a = (m**2 - n**2)
            b = 2*m*n
            c = (m**2 + n**2)
            print((d*a, d*b, d*c))
