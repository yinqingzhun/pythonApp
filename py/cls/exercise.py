# -*- coding:UTF-8 -*-
from enum import Enum


class Parrot(object):
    def __init__(self):
        self._voltage = 100000
        self.v = 135

    # property getter
    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage

    # property setter
    @voltage.setter
    def voltage(self, value):
        self._voltage = value

    @voltage.deleter
    def voltage(self):
        del self._voltage

    @classmethod
    def prname(cls):
        print(cls.__name__)

    @staticmethod
    def name():
        return Parrot.__name__


class Employee:
    # class property
    """员工基类"""
    empCount = 0

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
        self._t = 1
        Employee.empCount += 1

    @staticmethod
    def display_count():
        print("Total Employee %d" % Employee.empCount)

    def display_employee(self):
        print("Name : ", self.__name, ", Salary: ", self.__salary)


Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


class fooparent(object):
    def __init__(self):
        self.parent = 'i\'m the parent.'
        print('parent init')

    def bar(self, message):
        print("bar from parent : %s" % message)


class foochild(fooparent):
    def __init__(self):
        # 首先找到 foochild 的父类（就是类 fooparent），然后把类b的对象 foochild 转换为类 fooparent 的对象
        super(foochild, self)
        super(foochild, self).__init__()
        print('child init')

    def bar(self, message):
        super(foochild, self).bar(message)
        print('bar from child fuction : %s' % message)
        print(self.parent)


if __name__ == '__main__':
    foochild = foochild()
    foochild.bar('helloworld')
