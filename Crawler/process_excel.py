#!/usr/bin/python
#-*- coding:utf8 -*-
import xlrd
import xlwt
import sys
import os
reload(sys)
sys.setdefaultencoding( "utf8" )

#打开Excel文件
def read_excel(file):
    data = xlrd.open_workbook(file)
    #sheet对象
    table = data.sheets()[0]
    #nrows 表格总行数
    nrows = table.nrows
    #sheet二维列表，装载所有目标文件中的内容
    sheet=[]
    for i in range(nrows):
        #读取表格中的每一行内容
        temp_rows = table.row_values(i)
        rows = []
        for row in temp_rows:
        # 处理表格中单元格内容为空的内容
        #     if len(row)==0:
        #         row=0
            rows.append(row)
        sheet.append(rows)
    return sheet

#写入Excel
#content为二维列表
def write_excel(content,newfilename):
    f = xlwt.Workbook()
    sheet1= f.add_sheet(u'sheet1',cell_overwrite_ok=True)
    line_num = 0
    for row in content:
        for i in range(len(row)):
            if line_num<len(content):
                sheet1.write(line_num,i,row[i])
        line_num+=1
    f.save(newfilename)
    print newfilename+" 写入成功！"


if __name__ == "__main__":
    content = read_excel('linux.xls')
    unprocessed_excels_dir = "/Users/apple/downloads/unprocessed_excels/"
    unprocessed_excels = os.listdir(unprocessed_excels_dir)
    for temp in unprocessed_excels:
        filename_split = os.path.splitext(temp)
        if ".xlsx" in filename_split or ".xls" in filename_split:
            filename = unprocessed_excels_dir+temp
            content = read_excel(filename)
            processed_excels_dir = "/Users/apple/downloads/processed_excels/"
            newfilename = processed_excels_dir+ filename_split[0]+'.xls'
            if os.path.exists(processed_excels_dir) == False:
                os.mkdir(processed_excels_dir)
            else:
                write_excel(content,newfilename)


