#-*- coding:utf8 -*-
import tkinter as tk
import tkinter.messagebox
window = tk.Tk()
window.title('my window')
window.geometry('300x400')

'''
#Button
var=tk.StringVar()
l=tk.Label(window,textvariable=var,bg='red',font=('Arial,12'),width=10,heigh=2)
l.pack()
on_hit=False
def hit_me():
    global on_hit
    if on_hit==False:
        var.set('you hit me')
        on_hit=True
    else:
        var.set('')
        on_hit=False
b=tk.Button(window,text='hit me',width=10,height=2,command=hit_me)
b.pack()
'''

'''
#Entry
e=tk.Entry(window,show=None)
e.pack()
t=tk.Text(window,height=2)
def insert_point():
    var=e.get()
    t.insert('insert',var)
def insert_end():
    var=e.get()
    t.insert('1.1',var)
b1=tk.Button(window,text='insert point',width=15,height=2,command=insert_point)
b2=tk.Button(window,text='insert end',width=15,height=2,command=insert_end)
b1.pack()
b2.pack()
t.pack()
'''

'''
#Listbox
var1=tk.StringVar()
l=tk.Label(window,textvariable=var1,bg='yellow',height=2,width=10)
l.pack()
def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)
b=tk.Button(window,text='print selection',width='15',command=print_selection)
var2=tk.StringVar()
var2.set((11,22,33,44))
lb=tk.Listbox(window,listvariable=var2,bg='green')
list_items = [1, 2, 3, 4, 'first']
for item in list_items:
    lb.insert('end',item)
lb.pack()
b.pack()
'''

'''
#RadioButton
var=tk.StringVar()
l=tk.Label(window,text='Empty',height=2,width=20,bg='yellow')
l.pack()
def print_selection():
    l.config(text='you have selected'+var.get())
var2=tk.StringVar()
r1=tk.Radiobutton(window,text='option A',value='A',variable=var,command=print_selection)
r2=tk.Radiobutton(window,text='option B',value='B',variable=var,command=print_selection)
r3=tk.Radiobutton(window,text='option C',value='C',variable=var,command=print_selection)
r1.pack()
r2.pack()
r3.pack()
'''
'''
#scale用法
l=tk.Label(window,height=2,width=20,text='empty')
l.pack()
def print_selection(v):
    l.config(text="you have selected "+v)
s=tk.Scale(window,label='try me',from_=0,to=50,length=200,showvalue=0,tickinterval=10,resolution=0.1,orient=tk.HORIZONTAL,command=print_selection)
s.pack()
'''
'''
#Checkbutton
var1=tk.IntVar()
var2=tk.IntVar()
l=tk.Label(window,width=20,height=2,bg='yellow')
l.pack()
def print_selection():
    if (var1.get()==1)&(var2.get()==0):
        l.config(text='i love python')
    elif (var1.get()==0)&(var2.get()==1):
        l.config(text='i love c')
    elif (var1.get()==1)&(var2.get()==1):
        l.config(text='i love both')
    else:
        l.config(text='i do not love either')
c1=tk.Checkbutton(window,text='python',onvalue=1,offvalue=0,variable=var1,command=print_selection)
c2=tk.Checkbutton(window,text='c',onvalue=1,offvalue=0,variable=var2,command=print_selection)
c1.pack()
c2.pack()
'''
'''
#canvas
canvas=tk.Canvas(window,bg='blue',height=100,width=200)
image_file=tk.PhotoImage(file='ins.gif')
image=canvas.create_image(0,0,anchor='nw',image=image_file)
x1,x2,y1,y2=50,50,80,80
line=canvas.create_line(x1,x2,y1,y2)
oval=canvas.create_oval(x1,x2,y1,y2,fill='red')
arc=canvas.create_arc(x1+20,x2+20,y1+20,y2+20,fill='red',start=0,extent=180)
rect=canvas.create_rectangle(100,30,120,50)
def moveit():
    canvas.move(rect,5,5)
b=tk.Button(window,text='move',height=2,width=5,command=moveit)
canvas.pack()
b.pack()
'''
'''
#menubar
l=tk.Label(window,text='',bg='yellow')
l.pack()
menubar=tk.Menu(window)
filemenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
counter=0
def do_job():
    global counter
    l.config(text='do'+str(counter))
    counter+=1
filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
'''
'''
l=tk.Label(window,text='on the window')
l.pack()
frm=tk.Frame(window)
frm.pack()
frm_l=tk.Frame(frm)
frm_l.pack(side='left')
l1= tk.Label(frm_l,text='on the left window')
l3= tk.Label(frm_l,text='on the left window')
l1.pack()
l3.pack()
frm_r=tk.Frame(frm)
frm_r.pack(side='right')
l2= tk.Label(frm_r,text='on the right window')
l2.pack()
'''
'''
#messsagebox
def hit_me():
    # tk.messagebox.showinfo(title='hi',message='hello world')
    tk.messagebox.showwarning(title='hi',message='hello world')
    #  tk.messagebox.showerror(title='hi',message='hello world')
    # tk.messagebox.askquestion(title='hi',message='hello world')
b=tk.Button(window,text='hit me', command=hit_me)
b.pack()
'''
'''
#pack
tk.Label(window,text='1').pack(side='left')
tk.Label(window,text='1').pack(side='right')
tk.Label(window,text='1').pack(side='top')
tk.Label(window,text='1').pack(side='bottom')
'''
# grid
for i in range(4):
    for j in range(3):
        tk.Label(window,text='2').grid(row=i,column=j,padx=10,pady=10)
# place
tk.Label(window,text='place').place(x=50,y=200,anchor='se')
window.mainloop()