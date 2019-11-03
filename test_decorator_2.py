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


# 用装饰器 decorator_one 装饰函数 raw_func
@decorator_one
def raw_func():
    print 'hello world'

if __name__ == '__main__':
    # 看似我们执行的是 raw_func() 函数，实际上 raw_func 已经被
    # decorator_one装饰过了，真正执行的是经过装饰的函数
    raw_func()

    # 本来我们想要打印的是函数 raw_func 的名字
    # 事实却并不是如此，我们打印的是装饰器中的函数名，如果我们不像让这个函数的名字和注释文档
    # 被篡改，请见 test_decorator_3.py
    print raw_func.__name__

