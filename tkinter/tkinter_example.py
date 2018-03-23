#-*- coding:utf8 -*-
import tkinter as tk
window=tk.Tk()
window.title('my window')
window.geometry('500x400')
#canvas
canvas = tk.Canvas(window,height=200,width=440)
file_image=tk.PhotoImage(file='welcome.gif')
canvas.create_image(0,0,anchor='nw',image=file_image)
canvas.pack()
#username,password
tk.Label(window,text='Username:').place(x=50,y=150)
tk.Label(window,text='Password:').place(x=50,y=190)

#entry
username=tk.StringVar()
username.set('example@python.com')
tk.Entry(window,show=None).place(x=150,y=150)
tk.Entry(window,show='*',).place(x=150,y=190)


def login():
    pass

def signup():
    pass
#login,signup
tk.Button(window,text='Login',command=login).place(x=150,y=230)
tk.Button(window,text='Sign up',command=signup).place(x=270,y=230)
window.mainloop()

