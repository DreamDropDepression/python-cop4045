# -*- coding: utf-8 -*-
'''Solves Quadratic Equations and graphs results'''
import math

from pylab import rcParams
rcParams['figure.figsize'] = 5, 5


def get_val(val):
    '''Simple Input'''
    return float(input('Enter value for ' + val + ': '))

def discriminant(a, b, c):
    '''Calculates discriminant'''
    return b**2 - (4 * a * c)

def plus_quadratic(a, b, d):
    '''Positive solution for 2 solutions'''
    return (-b + math.sqrt(d)) / (2 * a)

def minus_quadratic(a, b, d):
    '''Positive solution for 2 solutions'''
    return (-b - math.sqrt(d)) / (2 * a)

def one_solution(a, b):
    '''For single solutions there isn't a need to separate'''
    return -b / (2 * a)

def output(a, b, d):
    '''Uses value of d to determine # of solutions with their values'''
    if d < 0:
        print('No real solutions.')
    if d == 0:
        print('One real solution: , x =', one_solution(a, b))
    if d > 0:
        print('Two real solutions: x1 =', plus_quadratic(a, b, d)\
        , ', x2 =', minus_quadratic(a, b, d))

def main():
    '''Main function'''
    while True:
        a = get_val('a')
        b = get_val('b')
        c = get_val('c')
        # important for number of solutions and their values
        d = discriminant(a, b, c)
        # prints number of solutions and their values
        output(a, b, d)
        # Lists will hold the coordinates
        xs = []
        ys = []
        # Outer bounds
        x_0 = -5.0
        x_1 = 5.0
        # Initial point and Number of points
        x = x_0
        n = 100
        # Step value
        dx = (x_1 - x_0) / n
        # Load the lists
        while x <= x_1:
            xs.append(x)
            y = a*x**2 + b*x + c
            ys.append(y)
            x += dx
        pylab.title('Quadratic Function')
        pylab.plot(xs, ys, '-bo')
        pylab.xlim(-6, 6)
        pylab.ylim(0, 10)
        pylab.show()
main()
