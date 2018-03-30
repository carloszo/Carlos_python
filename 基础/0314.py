#!/usr/bin/python
#-*- encoding:utf-8 -*-
#条件判断
age = 20
if age>=18:
  print "you are adult,your age is", age
  print("adult")
elif age >=6:
  print "teenager"
else:
  print "kid"

#循环
#for循环
names =["anni","carlos","ivan"]
for name in names:
  print name

sum =0

for x in [0,1,2,3,4,5,6,7,8,9]:
  sum =sum + x
print sum

#range()自动生成列表
sum1= 0
for y in range(101):
  sum1 = sum1+y
print sum1
print range(0,101)

#使用while循环
sum3 = 0
n = 0
while n<101:
  sum3 = sum3 + n
  n+=1
print sum3
#使用raw_input()
age = raw_input("birth:")
if age < 28:
  print "00后"
else:
  print "00前"

#字典
print "-------------------------------------"
dic = {"name":"carlos","age":30,"sex":"man"}
#增加数据
dic['lugar'] = "wuhan"
print dic["name"]
#判断是非存在某个key
print 'name' in dic
#删除key
dic.pop("name")
print dic

#set
s =set([1,1,2,4,2,3,5,6,5])
print s
#增加元素／删除元素
s.add(8)
print s
s.remove(1)
print s
#函数的使用
#取绝对值函数abs()
print "100的绝对值为：",abs(100)
print "-50的绝对值为：",abs(-50)
print "12.34的绝对值为：",abs(12.34)
#比较函数cmp()
print "2和3比较大小：", cmp(2,3)
print "5和2比较大小：",cmp(5,2)
#数据类型转换
print "str转换为int：",int('123')
print "float转换为int:",int(12.34)
print "int转换为str:",str(1.23)
