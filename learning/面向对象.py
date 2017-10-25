#!/usr/bin/python
# -*- coding: utf-8 -*-
import types


class Student(object):
    hello = 'dd'

    def __init__(self, name, score, age):
        # 注意到__init__方法的第一个参数永远是self，表示创建的实例本身
        # 普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self
        # 实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
        self.__name = name
        self.__score = score
        self.__age = age

    def print_score(self):
        print '%s :%s' % (self.__name, self.__score)

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = value

    @property
    def age(self):
        return self.__age

    '''只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，
    负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作'''

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__age = value

    # 相当于Java中的toString方法
    def __str__(self):
        return self.__name

    # __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串
    __repr__ = __str__


def fn():
    pass


def set_name(self, name):
    self.__name = name


if __name__ == '__main__':
    bart = Student('luchi', 13, 15)
    print bart.print_score()
    # 访问出错 ,没有该属性
    # print bart.__name
    print type(fn) == types.FunctionType
    # 获取一个对象所有属性和方法
    print dir(bart)
    print bart.__getattribute__('hello')
    # 上面的set_name方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能
    Student.set_name = set_name
    bart.age = 60
    print bart
