#!/usr/bin/python2
# -*- coding:UTF-8 -*-

class Parent(object):
    def __init__(self):
        self.parent = 'I\'m [parent]'
        print 'parent...'

    def func(self, message):
        print "%s from parent." % message

class Child(Parent):
    def __init__(self):
        super(Child, self).__init__()
        print 'child...'

    def func(self, message):
        super(Child, self).func(message)
        print '[child] func function'
        print self.parent

if __name__ == '__main__':
    c = Child()
    c.func('hello')

