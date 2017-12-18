# -*- coding:UTF-8 -*-
from enum import Enum


class Parrot(object):
    def __init__(self):
        self._voltage = 100000
        self.v = 135

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage

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
