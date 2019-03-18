# -*- coding: utf-8 -*-
"""Polynomial Class
    Supports operations such as addition and multiplication
    of polynomial objects.

    Coefficients are represented as lists.
    Position # in list is the degree of that coefficient.
"""


class Poly(object):
    '''Takes a list of coefficients to make a working polynomial type'''

    def __init__(self, coeffs):
        '''Assumes input is an integer or float'''
        self.degree = len(coeffs)
        self.coeffs = [float(c) for c in coeffs]

    def __str__(self):
        '''Converts to string representation'''
        out = ''
        for i, c in enumerate(self.coeffs):
            if c == 0.0:
                continue
            out += self.to_str(c, i)
        return out

    def __repr__(self):
        '''Printing at the terminal'''
        return 'Poly({})'.format(self.coeffs)

    def __getitem__(self, k):
        '''Fetches the coeffiecent that has degree k'''
        try:
            if 0 <= k <= self.degree:
                return self.coeffs[k]
            else:
                raise ValueError()
        except ValueError:
            print('Index out of range or non-integer')

    def __add__(self, poly2):
        '''Adds 2 polynomials Returns Poly'''
        upto = len(self.coeffs)
        result = []
        for i in range(len(self.coeffs)):
            result.append(self.coeffs[i] + poly2[i])
        for i in range(upto, len(poly2.coeffs)):
            result.append(poly2[i])
        return Poly(result)

    def __mul__(self, poly2):
        '''Multiplies 2 polynomials Returns Poly'''
        terms = {}
        for i, c in enumerate(self.coeffs):
            for j, c2 in enumerate(poly2.coeffs):
                terms[i+j] = terms.get(i+j, 0) + c*c2
        return Poly([terms[sums] for sums in terms.keys()])

    def __rmul__(self, k):
        '''Scalar multiplication. Returns Poly'''
        return Poly([k * self.coeffs[c] for c in range(len(self.coeffs))])

    def __eq__(self, poly2):
        '''Returns True if 2 polynomials are equal'''
        if self.coeffs == poly2.coeffs:
            return True
        else:
            return False

    def __ne__(self, poly2):
        '''Return True if 2 polynomials are not equal'''
        if self.__eq__(poly2):
            return False
        else:
            return True

    def eval(self, x):
        '''Computes Polynomial value'''
        sum = 0
        for i, c in enumerate(self.coeffs):
            if i == 0:
                sum += c
            if i >= 1:
                sum += c * (x**i)
        return sum

    def to_str(self, c, i):
        '''makes given term a string'''
        cstr = ''
        if i != 0:
            cstr += '  +  '
        if i == 0:
            cstr += '{}'.format(str(c))
        elif i == 1:
            cstr += '{}x'.format(str(c))
        elif i > 1:
            cstr += '{}x^{}'.format(str(c), str(i))
        return cstr


def TestPoly():
    def unittest(b, tname):
        result = 'FAILED'
        if b:
            result = 'PASSED'
        print('{:<15} : {:<10}'.format(tname, result))

    coeff = [1, 2, 3, 4]
    coef2 = [5, 6, 7, 8]
    passed = [1.0, 2.0, 3.0, 4.0]

    p = Poly(coeff)
    p2 = Poly(coef2)

    # Poly.init
    unittest(p.coeffs == passed, '__init__  ')
    # test str
    pstr = str(p)
    unittest(pstr == '1.0  +  2.0x  +  3.0x^2  +  4.0x^3', '__str__  ')

    # test repr
    prepr = repr(p)
    unittest(prepr == 'Poly([1.0, 2.0, 3.0, 4.0])', '__repr__  ')

    # test getitem
    pget = p.__getitem__(2)
    unittest(pget == 3.0, '__getitem__  ')

    # test add
    padd = p + p2
    unittest(str(padd) == '6.0  +  8.0x  +  10.0x^2  +  12.0x^3', '__add__')

    # test mul
    pmul = p * p2
    unittest(str(pmul) == '5.0  +  16.0x  +  34.0x^2  +  60.0x^3  +  61.0x^4\
                           +  52.0x^5  +  32.0x^6', '__mult__')

    # test rmul
    prmul = 3 * p
    unittest(str(prmul) == '3.0  +  6.0x  +  9.0x^2  +  12.0x^3', '__rmult__')

    # test eq
    peq = Poly(coeff)
    unittest(p == peq, '__eq__  ')

    # test neq
    pne = Poly(p.coeffs)
    unittest(p2 != pne, '__ne__  ')


if __name__ == '__main__':
    TestPoly()
