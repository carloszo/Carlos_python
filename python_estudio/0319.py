#!/usr/bin/python
#-*- coding:utf-8 -*-
#map和reduce函数使用方法
#map:map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。
def f(x):
  return x*x

print map(f,[1,2,3,4,5,6,7,8,9])
#利用map将数组中的元素转化为字符串
print map(str,[1,2,3,4,5,6,7,8,9])
#reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
#利用reduce给列表求和
def add(x,y):
  return x+y
L=[1,2,3,4,5,6,7,8,9]
print '利用reduce()给列表求和:',reduce(add,L)
print '利用sum()给列表求和:',sum(L)
#配合map()，我们就可以写出把str转换为int的函数：
def char2num(s):
  return{'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
def fn(x,y):
  return x*10+y

print reduce(fn,map(char2num,'267865'))
print map(char2num,'23654')
#利用lambda函数简化
def str2int(s):
  return reduce(lambda x,y:x*10+y,map(char2num,s))

print '使用str2int()将字符串转化为字符串:',str2int('78454')

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
s=['adam', 'LISA', 'barT']
def rightstr(s):
 return s[0].upper()+s[1:].lower()

print'利用map（）将手写字母大写：', map(rightstr,s) 
