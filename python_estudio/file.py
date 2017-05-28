#!/usr/bin/python
#-*- coding:utf-8 -*-
import os
#读文件
try:
    f = open("/Users/apple/documents/file.txt",'r')
    content = f.read()
    print content
finally:
    if f:
        f.close()

'''如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：'''

with  open("/Users/apple/documents/file.txt",'r') as f:
    for line in f.readlines():
        print line.strip()

#读二进制文件需要使用rb
try:
    f=open("/Users/apple/documents/1.jpg",'rb')
    content = f.read()
    print content
finally:
    if f:
        f.close()
#要读取非ASCII编码的文本文件，就必须以二进制模式打开，再解码。比如GBK编码的文件：
'''
try:
    f = open("/Users/apple/documents/file2.txt",'rb')
    content=f.read().decode('gbk')
    print content
finally:
    if f:
        f.close()
'''
#写文件

f=open("/Users/apple/documents/file2.txt",'w')
f.write('hello,world')
f.close()

#操作文件和目录
print '查看当前目录的绝对路径：%s'% os.path.abspath('.')

#创建目录
#生成新的目录地址
newdir=os.path.join('/Users/apple/documents/','carlos')

#获取当前目录下的所有目录
print'当前目录下的所有目录为：', [x for x in os.listdir('.') if os.path.isdir(x)]
#获取当前目录下的所有文件
print '当前目录下的所有文件为：',[x for x in os.listdir('.') if os.path.isfile(x)]
#获取当前目录下的所有后缀为py的文件
print '当前目录下的所有后缀为py的文件',[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

#练习：编写一个search(s)的函数，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出完整路径：

def search(name):
    list = os.listdir('.')
    for x in list:
        if os.path.splitext(x)[0] ==name:
            print os.path.join(os.path.abspath('.'),x)

search('0318')

