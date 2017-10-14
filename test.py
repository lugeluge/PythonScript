#!/usr/bin/env python3
#-*- coding:utf-8 -*-
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print('%s:%s'%(self.name,self.score))
lc = Student('lc',15)
lu=Student('lu',16)
lc.print_score()
lu.print_score()