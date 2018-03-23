#-*- coding:utf8 -*-
import numpy as np

#array
a=np.array([2,3,4,5,6],dtype=np.int16)#一维array，dtype可以指定数据格式
a=np.array([[1,2,3,4],[2,3,4,5]])#多维array
a=np.zeros((3,5))#生成为0的array，（3，5）中3表示行数，5表示列数。
a=np.arange(12).reshape(2,6) #有序数列，类似于python中的range(),reshape表示更改形状。
a=np.linspace(1,10,6) #linspace表示生成从1-10
# print(a)

#基础运算
a=np.array([10,60,50,70])
b=np.arange(4)
c=a+b#a和b中的元素会逐个相加
d=a-b#a和b中的元素会逐个相减
print('sin:',np.sin(a))#numpy中可以调用三角函数计算
print('a:',a)
print('b:',b)
print('a+b:',c)
print('a-b:',d)
print('b<3:',b<3)#b=array([0, 1, 2, 3]),b中的每一个元素会与3比较，返回结果为True,False的array
#矩阵运算
a=np.array([[1,2],
            [3,4]])
b=np.arange(4).reshape((2,2))
print(a)
print(b)
print('a*b:',a*b) #普通乘法，元素会逐个相乘
print(np.dot(a,b))#矩阵乘法，a.dot(b)另外一种表示方法
#array求和，最大值，最小值计算
a=np.random.random((2,4))#自动生成0-1之间的2行4列矩阵
print(a)
print('sum of a:',np.sum(a))
print('max of a:',np.max(a))
print('min of a:',np.min(a))

#axis=1表示在行中运算，axis=0表示在列中运算
print('sum of a,axis=1:',np.sum(a,axis=1))
print('sum of a,axis=0:',np.sum(a,axis=0))
print('max of a,axis=1:',np.max(a,axis=1))
print('max of a,axis=0:',np.max(a,axis=0))
print('min of a,axis=1:',np.min(a,axis=1))
print('min of a,axis=0:',np.min(a,axis=0))