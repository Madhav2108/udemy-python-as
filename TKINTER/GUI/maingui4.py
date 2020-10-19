from tkinter import *
win=Tk()
win.geometry("300x300")
def fun():
    l1=Label(win,text="hi....")
    print("Hi this a GUI Application Message....")
    l1.pack()
B=Button(win,text="Press Me",command=fun)
B.pack()
win.mainloop()