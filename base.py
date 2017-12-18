# -*- coding: utf-8 -*-
"""
this is cls page
"""

# import concurrent.futures.thread
import time
import types

import functools

from py.cls.exercise import Employee, Month


def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


lst = [1, 3, 5]
nlst = [1, 2, 3]
time_now = time.time();
s = '''hello
world''';
tuplev = (1, 3, 5)
dic = {}
dic['name'] = 'jack'
dic['age'] = 18
i = '101000'
x = set('runoob')
y = set('google')

s1 = time.clock()
list_2d = [1 for i in range(2)]
tuple2 = (1)


class a:
    id = "98173489"

    def getname(self):
        return "a"

    @classmethod
    def echo(cls, input):
        print('echo: ', input)


strs = "for i in range(0,10): print(i)"
c = compile(strs, '', 'exec')


def sqrt(p):
    return p ** 2


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


# if __name__ == '__main__':
#     foochild = foochild()
#     foochild.bar('helloworld')


# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return repr(value * 2)


s = 'a23g4hfd567'


# print(re.search('(?p<value>\d+)', s, re.m).groups())


# 为线程定义一个函数
def print_time(threadname, delay):
    count = 0
    print('ok')
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadname, time.ctime(time.time())))


# 创建两个线程
# try:
#     concurrent.futures.thread.start_new_thread(print_time, ("thread-1", 2,))
#     concurrent.futures.thread.start_new_thread(print_time, ("thread-2", 4,))
# except:
#     print
#     "error: unable to start thread"
#
# while 1:
#     pass
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def person(name, age, **kew):
    print('name:', name, 'age:', age, 'other:', kew)

    # def person(name, age, *, city, job):
    #     print(name, age, city, job, sep=",")
    #
    #
    # def person(name, age, *list, job, city):
    #     print(name, age, list, city, job, sep=",")


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Month)

for i,e in Month._member_map_.items():
    print(i,e,sep=",    ")