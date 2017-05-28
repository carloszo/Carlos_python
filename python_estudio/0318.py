#!/usr/bin/python
#-*- coding:utf-8 -*-
#切片
L=['carlos','anni','ivan','juan','maidee']
#从0开始，直到索引3为止
print L[0:3]
#如果第一个是0可以省略
print L[:3]
#从1开始，到3为止，取2个元素
print L[1:3]
#取倒数2个
print L[-2:]
#取倒数第二个
print L[-2:-1]

#利用切片取出数列中的一段数
L2=range(100)
#取出前10个数
print L2[:10]
#取出后10个数
print L2[-10:]
#取出11-20
print L2[10:20]
#前10个数，每两个取一个
print L2[:10:2]
#所有的数，每5个取一个
print L2[::5]
#元组也可以进行切片操作
T=(0,1,2,3,4,5,6,7,8,9)
print T[:3]
#用一句话生成列表
#生成1*1，2*2，3*3...
print [x*x for x in range(1,11)]
#生成式后面还可以加上if判断
print [x*x for x in range(1,11) if x%2==0]
#使用两层循环可以生成全排列
print [m+n for m in 'xyz' for n in 'abc']
#for循环使用2个变量取出字典
d={'name':'carlos','age':'30','city':'wuhan'}
for k,v in d.iteritems():
  print k,'=',v
#使用个变量生成列表
print [k+'='+v for k,v in d.iteritems()]

#把list中所有字符串变成小写
L3=['CARLOS','ANNI','IVAN']
print [s.lower() for s in L3]
#使用isinstance函数判断变量是不是字符串
x='abc'
y=123
print isinstance(x,str)
print isinstance(y,str)
#生成器
#生成器仅保存算法，创建生成器的方法很简单，只需要将生成式的[]改为（）
g = (x*x for x in range(1,11))
#使用for循环可取出生成器中的内容
for n in g:
  print n

#斐波拉契数列
def fib(max):
  n,a,b =0,0,1
  while n<max:
    print b
    a,b = b,a+b
    n=n+1
fib(6)

