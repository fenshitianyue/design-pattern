#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Singleton(object):
    """
    单例类装饰器，理论上可以用于想实现单例模式的任何类(单线程)
    """
    def __init__(self, cls):
        """参数是一个类"""
        self._cls = cls

    def Instance(self):
        """返回真正的实例"""
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError('singleton must be accessed through `Instance()`.')

    def __instance_check__(self, inst):
        """docstring for __instance_check__"""
        return isinstance(inst, self._decorated)

@Singleton
class A:
    """
    一个需要单例模式实现的类
    """
    def __init__(self):
        pass

    def display(self):
        return id(self)

if __name__ == '__main__':
    s1 = A.Instance()
    print s1, s1.display()

    s2 = A.Instance()
    print s2, s2.display()





