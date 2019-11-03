#!/usr/bin/python2
# -*- coding:UTF-8 -*-

from functools import wraps

"""
这是一段用于打印日志的装饰器代码模板
"""


def log_it(f):
    @wraps(f)
    def with_logging(*args, **kwargs):
        print '[ ' + f.__name__ + ' ] was called...'
        return f(*args, **kwargs)
    return with_logging

@log_it
def test_func():
    print 'hello world'

if __name__ == '__main__':
    test_func()
