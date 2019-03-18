# -*- coding: utf-8 -*-


class Employee(object):
    def __init__(self, name, phone, sal):
        self._name = name
        self._phone = phone
        self._sal = float(sal)

    def __str__(self):
        return '\n{}: {}; phone: {}; sal: {:<.2f}'.format(
            self.__class__.__name__,
            self._name,
            self._phone,
            self.sal_total())

    def __repr__(self):
        return "\n{}('{}', '{}', {:<.2f})".format(
            self.__class__.__name__,
            self._name,
            self._phone,
            self.sal_total())

    def sal_total(self):
        '''Returns the total salary'''
        return self._sal

    def name(self):
        '''Returns a string'''
        return self._name

    def phone(self):
        '''Returns a string'''
        return self._phone

    def sal(self):
        return self._sal


class Manager(Employee):
    '''Employee that has a bonus'''

    def __init__(self, name, phone, sal, bonus):
        Employee.__init__(self, name, phone, sal)
        self._bonus = float(bonus)

    def sal_total(self):
        return self._sal + self._bonus


class Ceo(Manager):
    def __init__(self, name, phone, sal, bonus, stock):
        Manager.__init__(self, name, phone, sal, bonus)
        self._stock = float(stock)

    def sal_total(self):
        return self._sal + self._stock + self._bonus


class Engineer(Employee):
    def __init__(self, name, phone, sal):
        Employee.__init__(self, name, phone, sal)


def print_staff(staff):
    for s in staff:
        print(repr(s))


def list_staff():
    en = Engineer('Wilbert', '4567890', 70000)
    en2 = Engineer('Doug', '7891234', 70000)
    m = Manager('Phil', '1233456', 50000, 10000)
    em = Employee('Pam', '1234567', 60000)
    em2 = Employee('Randy', '1233333', 55000)
    c = Ceo('Hojo', '1234444', 800000, 10000, 400000)

    return [en, m, em, c, en2, em2]


if __name__ == '__main__':
    print_staff(list_staff())
