#!/usr/bin/python
#-*- encoding:utf-8 -*-
#定义函数
print "自定义一个求绝对值的函数"
def my_abs(x):
  if x>=0:
    return x
  else:
    return -x
print "调用my_abs(),-100的绝对值为：",my_abs(-100)

#空函数
def nop():
  pass
  if age >=18:
    pass
print "pass起到占位作用，缺少pass，代码运行会有语法错误"

print "使用isinstance（)检测类型"
L = [2,1,4,6]
if isinstance(L,list):
  print "L is list"

#函数的参数
def power(x,n=2):
  sum = 1
  while n>0:
    sum = sum*x
    n-=1
  return sum

print power(2,10)

def enroll(name,gender,age=6,city="wuhan"):
  print "name:",name
  print "gerder:",gender
  print "age:",age
  print "city:",city

enroll("carlos","M",30)
print "----------------------------------"
enroll("ivan","M")
print "----------------------------------"
enroll("anni","F",city="beijing")
print "----------------------------------"

#默认参数不能是可变对象
def add_end(L=[]):
  L.append("END")
  return L
#如果add_end()正常调用时，没有问题
#print add_end([1,2,3,4])
#如果使用默认参数调用，问题则会很大
print add_end()
print add_end()
print add_end()

#正确的做法为
def add_end2(L=None):
  if L is None:
    L=[]
  L.append("ENd")
  return L

print add_end2()
print add_end2()
print add_end2([1,2,3,4,5,6,7,8])

#可变参数
#a，b，c……，请计算a2 + b2 + c2 + ……。
def calc(numbers):
  sum = 0
  for n in numbers:
    sum = sum +n*n
  return sum
print calc((1,2,3,4))
