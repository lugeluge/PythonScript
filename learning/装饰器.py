#!/usr/bin/python
# -*- coding: utf-8 -*-
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args ,**kw):
        print ('call %s()'%func.__name__)
        return func(*args,**kw)
    return wrapper
def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print '%s %s():'%(text,func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator
@log
def now():
    print '2017'
@logger('陆驰')
def nowwer():
    print '10/21'
if __name__ == '__main__':
    now()
    nowwer()
    print nowwer.__name__