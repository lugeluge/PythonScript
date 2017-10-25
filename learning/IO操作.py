#!/usr/bin/python
# -*- coding: utf-8 -*-
import io

#with语句来自动帮我们调用close()方法,是个好习惯
with open('hello.txt','r') as f:
    #f.write('hello')
    print f.read()
