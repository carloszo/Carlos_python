#!/usr/bin/python
#-*- coding:utf8 -*-
import xlrd
import sys
reload(sys)
sys.setdefaultencoding( "utf8" )
#打开Excel文件
data = xlrd.open_workbook('excel.xls')
table = data.sheets()[0]
nrows = table.nrows
tu=['奥林花园店','东澜岸店','丽华店','沔州大道店','民主路店','名都花园店','青城华府店','青宜居店','涂家岭店','孝感北京二路店','永旺经开店','友谊国际店']
liao =['城花璟苑店','均大店','马沧湖店','玫瑰二店','玫瑰街店','庙山店','琴台大道店','五里新村店','永旺金桥店','知音东村店','佛祖岭店']
li = ['百隆东方城店','宝丰二路店','常青花园店','楚天金园店','东立国际店','汉中路店','后湖东方店','荟聚店','金银潭店','泰福堂店','唐家墩店','新花莲店','中心店','紫润店'
,'东立国际店','宝丰二路店']
cai=['文华路店','汉城店','麦迪森店','七里店','太康店','太子水榭店','团结新村店']
sell_list=[]
for i in range(nrows):
    #print(str(table.row_values(i)).decode('unicode escape').encode('utf8'))
    s1 = table.row_values(i)[1]
    dianming=s1.replace('好药师','')
    xiaoshou = table.row_values(i)[11]
    maoli = table.row_values(i)[14]
    quyu=''
    if dianming in tu:
        quyu='廖燕妮'
    elif dianming in tu:
        quyu='涂梦云'
    elif dianming in li:
        quyu='李宁'
    elif dianming in cai:
        quyu='蔡静'
    sell_list.append((dianming,xiaoshou,maoli,quyu))


print sell_list[2]
    #s2=str(table.row_values(i)[11])
    #s3=str(table.row_values(i)[14])
    #print(type(s1),type(s2),type(s3))
    #print(s1+' '+s2 +' '+s3)
    #print a

#print(table.row_values(0)[11])
#print(table.row_values(0)[14])
#print(str(table.row_values(1)).decode('unicode escape').encode('utf8'))
#print(table.row_values(0)[1],table.row_values(0)[11],table.row_values(0)[14])