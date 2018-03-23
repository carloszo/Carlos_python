from tkinter import *
from tkinter.filedialog import askopenfilename
#!/usr/python/bin
#-*- coding:utf8 -*-
root = Tk()

#filename=askopenfilename(filetypes=(('txt files','*.txt'),('All files','*.*')))
#print filename
def helloButton():
    print 'hello button'
    filename=askopenfilename(filetypes=(('pdf files','*.pdf'),('all files','*.*')))
button = Button(root,text="button",command=helloButton)
input = Entry(root,text='please select the right pdf file')
button.grid(row=1,column=1)
input.grid(row=1,column=2)
root.mainloop()