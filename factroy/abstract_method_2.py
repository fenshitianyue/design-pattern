#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import abc
import six

class BasicCourse(object):
    def get_labs(self):
        return 'basic_course: labs'

    def __str__(self):
        return 'BasicCourse'

class ProjectCourse(object):
    def get_labs(self):
        return 'project_course: labs'

    def __str__(self):
        return 'ProjectCourse'

class LinuxVM(object):
    """Linux虚拟机"""
    def start(self):
        return 'Linux Virtual Machine Running...'

class MacVM(object):
    def start(self):
        return 'Mac OS Virtual Machine Running...'

@six.add_metaclass(abc.ABCMeta)
class Factory(object):
    """抽象工厂类"""
    @abc.abstractmethod
    def create_course(self):
        pass

    @abc.abstractmethod
    def create_vm(self):
        pass

class BasicCourseLinuxFactory(Factory):
    def create_course(self):
        return BasicCourse()

    def create_vm(self):
        return LinuxVM()

class ProjectCourseMacFactory(Factory):
    def create_course(self):
        return ProjectCourse()

    def create_vm(self):
        return MacVM()

def get_factory():
    return random.choice([BasicCourseLinuxFactory, ProjectCourseMacFactory])()

if __name__ == '__main__':
    factroy = get_factory()
    course = factroy.create_course()
    vm = factroy.create_vm()
    print course.get_labs()
    print vm.start()
