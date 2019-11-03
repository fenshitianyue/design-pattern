#!/usr/bin/python2
# -*- coding:UTF-8 -*-

from functools import wraps

# 装饰器
def decorator_one(func):
    # 包装你想"修饰的函数"的函数
    # @warps接受一个函数来进行修饰并加入了复制函数名称、注释文档、参数列表等功能
    # 这让我们在装饰器里面可以访问装饰之前的函数的属性
    @wraps(func)
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
    # 如上所见，当我们对装饰器做了如上修改后，就达到了2中我们想要的效果
    print raw_func.__name__

