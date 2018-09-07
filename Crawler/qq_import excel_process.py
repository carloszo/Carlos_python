#!/usr/bin/python
#-*- coding:utf8 -*-
import xlrd
import xlwt
import sys
import os
reload(sys)
sys.setdefaultencoding( "utf8" )


'''
姓名       :1
昵称        :2
QQ号       :3
家庭手机    :4	
工作手机    :5	
其他手机    :6
家庭电话    :7	
工作电话    :8	
其他电话    :9	
家庭传真    :10	
工作传真    :11	
公司/部门   :12
家庭地址    :13	
工作地址    :14	
其他地址    :15	
备注       :16	
电子邮件    :17	
家庭邮箱    :18	
办公邮箱	   :19
网址	       :20
家庭网址	   :21
办公网址    :22
生日        :23	
职务        :24
'''
#需处理文件所在目录
file_dir = "/Users/apple/Downloads/processed_excels/"

#打开Excel文件
def read_excel(file):
    data = xlrd.open_workbook(file)
    #sheet对象
    table = data.sheets()[0]
    #nrows 表格总行数
    nrows = table.nrows
    #sheet二维列表，装载所有目标文件中的内容

    #test
    # row1 = table.row_values(1)
    # print row1[0],row1[2],row1[3][4:]
    #end test

    sheet=[]
    for i in range(1,nrows):
        #读取表格中的每一行内容
        temp_row = table.row_values(i)
        row = []
        if len(temp_row[8])<1:
            continue
        elif len(temp_row)>0:
            name = temp_row[0] #姓名
            # print name
            # company_name = temp_row[0]
            tel_num = temp_row[8] #电话号码
            # print tel_num
            email = temp_row[9] #邮箱
            # print email
            profession = temp_row[2] #职务
            # print profession

            row = [name,tel_num,email,profession]
            sheet.append(row)
    return sheet

#写入Excel
#content为二维列表
def write_excel(content,filename):
    data = xlrd.open_workbook(file_dir+"import-2.xls")
    table = data.sheets()[0]
    first_row = table.row_values(0)
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
    line_num = 0
    for i in range(len(first_row)):
        sheet1.write(line_num, i, first_row[i])
    line_num = 1

    for row in content:
        if line_num<len(content):
            # [name, tel_num, email, profession]
            sheet1.write(line_num, 0, row[0])       #姓名
            sheet1.write(line_num, 5, row[1])       #工作电话
            # print row[1]
            sheet1.write(line_num, 15, row[2])       # 邮箱
            # print row[2]
            # sheet1.write(line_num, 12,row[2])       #公司名
            sheet1.write(line_num, 24, row[3])  # 职务
            # print row[3]
        line_num+=1
    print " 写入完成！"
    f.save(filename)
    # f = xlwt.Workbook()
    # sheet1= f.add_sheet(u'sheet1',cell_overwrite_ok=True)
    # line_num = 0
    # for row in content:
    #     for i in range(len(row)):
    #         if line_num<len(content):
    #             sheet1.write(line_num,i,row[i])
    #     line_num+=1
    # f.save(newfilename)
    # print newfilename+" 写入成功！"


if __name__ == "__main__":
    target_dir = file_dir + "PT/"
    unprocessed_excels = os.listdir(target_dir)
    for temp in unprocessed_excels:
        filename_split = os.path.splitext(temp)
        if ".xlsx" in filename_split or ".xls" in filename_split:
            filename = target_dir+temp
            content = read_excel(filename)
            processed_excels_dir = target_dir+"processed_excels/"
            newfilename = processed_excels_dir+ filename_split[0]+'_import.xls'
            if os.path.exists(processed_excels_dir) == False:
                os.mkdir(processed_excels_dir)
            else:
                write_excel(content,newfilename)
