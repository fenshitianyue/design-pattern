#!/usr/bin/python
# -*- coding:UTF-8 -*-


class Query(object):
    class _query(object):
        def __init__(self, sql):
            self.sql = sql

        def display(self):
            return id(self)

        def get_result(self):
            return self.sql
    _instance = None

    def __init__(self, sql):
        if Query._instance is None:
            Query._instance = Query._query(sql)

    def __getattr__(self, attr_name):
        return getattr(self._instance, attr_name)

if __name__ == '__main__':
    s1 = Query('select * from test1')
    print s1.display()
    print s1.get_result()

    s2 = Query('update test1 set field1 = value')
    print s1.display()
    print s2.get_result()

