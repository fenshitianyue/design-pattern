#!/usr/bin/python2
# -*- coding:UTF-8 -*-

from functools import wraps

class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile
    def __call__(self, f):
        @wraps(f)
        def wrapped_func(*args, **kwargs):
            log_string = '[ ' + f.__name__ + ' ] was called...'
            print log_string
            with open(self.logfile, 'a') as open_file:
                open_file.write(log_string + '\n')
            self.notify()
            return f(*args, **kwargs)
        return wrapped_func

    def notify(self):
        pass

@logit()
def func():
    print 'hello world'

if __name__ == '__main__':
    func()
