#!/usr/bin/python
#-*- coding:utf8 -*-
import tkinter as tk
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator
from tkinter.filedialog import askopenfilename
import tkinter.messagebox
window = tk.Tk()
window.title('PDF to TXT')
window.geometry('300x200')
lb = tk.Label(window,text='')
var=tk.StringVar()

def xz():
    filename = askopenfilename(filetypes=(('pdf files', '*.pdf'), ('all files', '*.*')))
    var.set(filename)
    if filename!='':
        lb.config(text='the file you selected is:'+filename)
    else:
        lb.config(text='you didnot select a file ' )
def pdf2txt():
    filename=var.get()
    if filename !='':
        #filename='我的简历.pdf'
        newfilename=filename[:-4]+'.txt'
        fp = open(filename, 'rb')
        #来创建一个pdf文档分析器
        parser = PDFParser(fp)
        #创建一个PDF文档对象存储文档结构
        document = PDFDocument(parser)
        # 检查文件是否允许文本提取
        if not document.is_extractable:
            raise PDFTextExtractionNotAllowed
        else:
            # 创建一个PDF资源管理器对象来存储共赏资源
            rsrcmgr=PDFResourceManager()
            # 设定参数进行分析
            laparams=LAParams()
            # 创建一个PDF设备对象
            # device=PDFDevice(rsrcmgr)
            device=PDFPageAggregator(rsrcmgr,laparams=laparams)
            # 创建一个PDF解释器对象
            interpreter=PDFPageInterpreter(rsrcmgr,device)
            # 处理每一页
            for page in PDFPage.create_pages(document):
                interpreter.process_page(page)
                # 接受该页面的LTPage对象
                layout=device.get_result()
                for x in layout:
                    if(isinstance(x,LTTextBoxHorizontal)):
                        with open(newfilename,'a') as f:
                            f.write(x.get_text().strip().encode('utf-8')+'\n')
    else:
        tk.messagebox.showwarning('错误','没有选择文件！')


# lb.pack()

b1=tk.Button(window,text='选择',height=2,width=10,command=xz)
b2=tk.Button(window,text='转换',height=2,width=10,command=pdf2txt)
b1.pack()
b2.pack()
window.mainloop()