#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

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

class SimpleCourseFactory(object):
    @staticmethod
    def create_course(type):
        """简单工厂，用于创建课程"""
        if 'bc' == type:
            return BasicCourse()
        elif 'pc' == type:
            return ProjectCourse()


if __name__ == '__main__':
    t = random.choice(['bc', 'pc'])
    course = SimpleCourseFactory.create_course(t)
    print course.get_labs()
