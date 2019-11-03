#!/usr/bin/python2
# -*- coding:UTF-8 -*-

from functools import wraps

class log_it(object):
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

# log_it 的子类，更具体的执行某类通知日志
class email_log_it(log_it):
    """
    在函数调用后发送email给管理员
    """
    def __init__(self, email='admin@some.com', *args, **kwargs):
        self.email = email
        super(email_log_it, self).__init(*args, **kwargs)

    def notify(self):
        """
        发送一份email给管理员，暂不实现
        """
        pass

@log_it()
def func():
    print 'hello world'

if __name__ == '__main__':
    func()
