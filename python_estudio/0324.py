#!/usr/bin/python
#-*- coding:utf-8-*-
import functools
#sorted()的用法
L = [23,24,12,45,6,43]
print '顺序排列：',sorted(L)
#sorted()为高阶函数，可以附带方法，利用sorted进行倒序排列。
def sorted_reverse(x,y):
    if x>y:
       return -1
    if x<y:
        return 1
    return 0
print '倒序排列：',sorted(L,sorted_reverse)

#利用sorted进行字母排序
L2 =['Carlos','ma','anni','ivan','Juan',]
def sorted_letter(x,y):
    s1=x.upper()
    s2=y.upper()
    if s1>s2:
        return 1
    if s1<s2:
        return -1
    return 0
print '字母排序：',sorted(L2,sorted_letter)

#偏函数的用法
#例如int()函数，当传入参数默认为字符串时，可以默认按十进制转化，但可以传入base参数，按照参数进制转换。
print '按照八进制转换：',int('123456',base=8)
#当需要转换大量二进制数据时，使用base特别麻烦，可以定义int2()函数

#def int2(x,base=2):
#   return  int(x,base)
#print int2('100000')
#其实可以使用functools.partial创建int2(),需要导入functools
int2=functools.partial(int,base=2)
print '使用functools.partial创建int2()并转化二进制为10进制:', int2('101001')
