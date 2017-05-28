#!/usr/bin/python
#-*- coding:utf-8 -*-
#关键词参数
def person(name,age,**kw):
  print 'name:',name,'age:',age,'other:',kw
#可以放一个关键词参数
person('carlos',30,city='wuhan')
#可以放多个关键词参数
person('anni',30,gender='F',city='wuhan')
#可以把多个关键词参数封装在一个字典中
kw ={'city':'wuhan','job':'ingeniero'}
person('ivan',4,city=kw['city'],job=kw['job'])
#简单的写法为
person('ivan',4,**kw)
print '----------------------------'
#使用一个函数总结必选参数、默认参数、可变参数、关键词参数的研发
def func(a,b,c=0,*args,**kw):
  print 'a =',a,'b =',b,'c = ',c,'args = ',args,'kw =',kw

func(1,2)
func(1,2,3)
func(1,2,3,'a','b')
func(1,2,3,'a','b',x=99)

#可以通过元组和字典调用函数
print '通过元组和字典调用函数'
args=(1,2,3,4,5)
kw={'x':100,'y':200}
func(*args,**kw)

print '--------------------------------'
print '递归函数'
def fact(n):
  if n ==1:
    return 1
  return n*fact(n-1)

print fact(5)
print fact(10)
print fact(20)
#尾递归，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
def fact2(n):
  return fact_iter(n,1)

def fact_iter(num,sum):
  if num == 1:
    return sum
  return fact_iter(num-1,num*sum)
print '使用尾递归计算'
print fact2(5)
print fact2(100)
