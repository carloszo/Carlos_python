#!/usr/bin/python
#-*- coding:utf-8 -*-

#使用__slots__只允许实例添加某些熟悉

class Student(object):
    __slots__=('name','age')
    pass

#可以给实例绑定属性

carlos = Student()
carlos.name="carlos"
print carlos.name
#carlos.city="wuhan" 其它属性添加不进去
