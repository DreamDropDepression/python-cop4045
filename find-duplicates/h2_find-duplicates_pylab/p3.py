# -*- coding: utf-8 -*-
'''Evaluates user's equation, then prints a table and graph of results'''
import math
import pylab


def main():
    '''Takes input, computes and displays results'''
    fun_str = input('Enter function with variable x: ')
    ns = float(input('Enter number of samples: '))
    xmin = float(input('Enter xmin: '))
    xmax = float(input('Enter xmax: '))
    x = xmin
    xs = []
    ys = []
    dx = (xmax - xmin) / ns
    while x <= xmax:
        xs.append(x)
        y = eval(fun_str)
        ys.append(y)
        x += dx
    print(xs)
    print(ys)
    print('{:>20s}{:>20s}'.format('x', 'y'))
    print('-' * 40)
    for i in enumerate(range(len(xs))):
        print('{:>20.4f}{:>20.4f}'.format(xs[i], ys[i]))

    pylab.title(fun_str)
    pylab.plot(xs, ys, '-bo')
    pylab.xlim(xmin, xmax)
    pylab.ylim(min(ys), max(ys))
    pylab.show()


main()
