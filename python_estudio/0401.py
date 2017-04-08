#!/usr/bin/python
#-*- coding:utf-8 -*-
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    
    def print_score(self):
        print '%s:%s'%(self.name,self.score)

    def get_grade(self):
        if self.score >=80:
            return 'A'
        elif self.score>=60:
            return 'B'
        else:
            return 'C'


carlos = Student('carlos',25)
carlos.print_score()
print carlos.get_grade()

# 如果不想让内部属性在外部被访问，可以在变量前使用两个下划线__，将变量变为私有变量。
class Student2(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def get_name(self):
        return self.__name

anni = Student2('anni',70)
print anni.get_name()

#类的继承
class Animal(object):
    def run(self):
        print "animal is running"

class Dog(Animal):
    pass
# 子类可以继承父类的所有方法，也可以增加新方法，
    def eat(self):
        print "eating meat"
# 子类还可以对父类的方法进行修改，例如修改父类的run方法
    def run(self):
        print "Dog is running"
dog = Dog()
dog.run()
dog.eat()

#__slots__的使用
