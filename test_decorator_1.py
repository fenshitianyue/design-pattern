#!/usr/bin/python2
# -*- coding:UTF-8 -*-

# 装饰器
def decorator_one(func):
    # 包装你想"修饰的函数"的函数
    def wrap_the_func():
        print 'do some work before func()'
        func()
        print 'do some work after func()'
    # 返回经过包装后的函数
    return wrap_the_func

def raw_func():
    print 'hello world'

if __name__ == '__main__':
    # 用装饰器 decorator_one 装饰函数 raw_func,返回一个经过装饰的函数
    func = decorator_one(raw_func)
    func()

