#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
# File Name: decorator.py
# Author: imguagua
# mail: harry.fan@foxmail.com
# Created Time: 2016-07-15
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('call %s %s():' % (text,func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('my func')
def now():
    print('2016-11-11')

now()
