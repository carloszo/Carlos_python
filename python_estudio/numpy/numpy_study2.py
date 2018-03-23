#!/usr/bin/python
#-*- coding:utf8 -*-
import numpy as np


#一维数组切片
a=np.arange(10)
print(a)
#print("a[0,1]=",a[0,1])
print("a[3:7]=",a[3:7])
#前面7个数，每三个为间隔
print("a[:7:3]=",a[:7:3])
#翻转
print("a[::-1]=",a[::-1])
a=np.arange(24).reshape(2,3,4)
print(a)
print('--------------------------多维数组选取--------------------------')
print('a[0,0,0]=',a[0,0,0])
#所有层的第一行第一列
print('a[:,0,0]=',a[:,0,0])
#第一层的所有行所有列
print('a[0,:,:]=',a[0,:,:])
#多个:可用...代替
print('a[0,:,:]=',a[0,...])
#第一层第二列，以2为间隔
print('a[0,1,::2]=',a[0,1,::2])
#所有楼层第二列房间
print('a[:,:,1]=',a[:,:,1])
#所有楼层第二行房间
print('a[:,1]=',a[:,1])
#如果要选取第1层楼的所有位于第2列的房间，在对应的两个维度上指定即可:
print('a[0,:,1]=',a[0,:,1])
#如果要选取第1层楼的最后一列的所有房间，使用如下代码:
print('a[0,:,-1]=',a[0,:,-1])
#如果要反向选取第1层楼的最后一列的所有房间，使用如下代码:
print('a[0,::-1,-1]=',a[0,::-1,-1])
#在该数组切片中间隔地选定元素:
print('a[0,::2,-1]=',a[0,::2,-1])
#多维数组翻转
print('a[::-1]=',a[::-1])
print('--------------------------改变数组的维度--------------------------')
print(a)
#(1)ravel 我们可以用ravel函数完成展平的操作:
print(a.ravel())
#(2)flatten 这个函数恰如其名，flatten就是展平的意思，与ravel函数的功能相同。
# 不过，flatten函数会请求分配内存来保存结果，而ravel函数只是返回数组的一个视图(view):
print(a.flatten())
b=a.reshape(6,4)
print(b)
#transpose 在线性代数中，转置矩阵是很常见的操作。对于多维数组，我们也可以这样做:
print(b.transpose())
a.shape=(6,4)
print(a)
print('--------------------------数组组合--------------------------')
a=np.arange(9).reshape(3,3)
print(a)
b=a*2
print(b)
#水平组合
print(np.hstack((a,b)))
#利用函数concatenate实现水平组合
print(np.concatenate((a,b),axis=1))
#垂直组合的两种方式
print(np.vstack((a,b)))
print(np.concatenate((a,b),axis=0))
#深度组合，就是将一系列数组沿着纵轴(深度)方向进行层叠组合。
# 举个例子，有若干张二维平 面内的图像点阵数据，
# 我们可以将这些图像数据沿纵轴方向层叠在一起，这就形象地解释了什么 是深度组合。
print(np.dstack((a,b)))
#列组合 column_stack函数对于一维数组将按列方向进行组合，如下所示:
print(np.column_stack((a,b)))
# 而对于二维数组，column_stack与hstack的效果是相同的
print(np.column_stack((a,b))==np.hstack((a,b)))
#行组合 当然，NumPy中也有按行方向进行组合的函数，它就是row_stack。
# 对于两个一维数组，将直接层叠起来组合成一个二维数组。
print(np.row_stack((a,b)))
#对于二维数组，row_stack与vstack的效果是相同的:
print(np.row_stack((a,b))==np.vstack((a,b)))
print('--------------------------数组分割--------------------------')
#(1) 水平分割 下面的代码将把数组沿着水平方向分割为3个相同大小的子数组:
print('水平分割')
print(a)
print(np.hsplit(a,3))
#对同样的数组，调用split函数并在参数中指定参数axis=1，对比一下结果:
print(np.split(a,3,axis=1))
#(2)垂直分割 vsplit函数将把数组沿着垂直方向分割:
print('垂直分割')
print(np.vsplit(a,3))
print(np.split(a,3,axis=0))
#(3) 深度分割 不出所料，dsplit函数将按深度方向分割数组。
print('深度分割')
a=np.arange(24).reshape(2,3,4)
print(a)
print(np.dsplit(a,4))
print('--------------------------数组的属性--------------------------')
print('数组的维度')
print(a.ndim)
print('数组的元素个数')
print(a.size)
print('我们可以使用tolist函数将NumPy数组转换成Python列表。')
print(a.tolist())
print('--------------------------常用函数--------------------------')
#(1) 单位矩阵，即主对角线上的元素均为1，其余元素均为0的正方形矩阵。
# 在NumPy中可以 用eye函数创建一个这样的二维数组，
# 我们只需要给定一个参数，用于指定矩阵中1的元素个数。 例如，创建2×2的数组:
i2=np.eye(2)
print(i2)
#使用savetxt函数将数据存储到文件中，当然我们需要指定文件名以及要保存的数组。
np.savetxt('eye.txt',i2)
#csv读取
print('读取CSV')
#NumPy中的loadtxt函数可以方便地读取CSV 文件，自动切分字段，并将数据载入NumPy数组。

xiaoshou,maoli,mubiao_xiaoshou = np.loadtxt('data.csv',skiprows=1,delimiter=',',usecols=(6,9,5),unpack=True)
print(xiaoshou)
# print(maoli)
# print(maoli/xiaoshou)
print(mubiao_xiaoshou)
#加权平均值
vwap=np.average(xiaoshou,weights=mubiao_xiaoshou)
print(vwap)