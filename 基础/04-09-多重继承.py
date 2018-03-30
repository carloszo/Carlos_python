#!/usr/bin/python
#-*- coding:utf-8 -*-
class Animal(object):
    pass

#大类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

#现在，我们要给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类：

class Runnable(object):
    def run(self):
        print "running"

class Flyable(object):
    def fly(self):
        print "flying"

#各种动物,对于需要Runnable功能的动物，就多继承一个Runnable，对于需要Flyable功能的动物，就多继承一个Flyable。
class Dog(Mammal,Runnable):
    pass

class Bat(Mammal,Flyable):
    pass

class Parrot(Bird,Flyable):
    pass

class Ostrich(Bird,Flyable):
    pass
