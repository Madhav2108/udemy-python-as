from tkinter import *
win=Tk()
win.geometry("300x300")
rL=Label(win,text="Red",bg="red",fg="white")
rL.pack()
gL=Label(win,text="blue",bg="blue",fg="white")
gL.pack(fill=X)
bL=Label(win,text="green",bg="green",fg="white")
bL.pack(fill=Y,side=LEFT)
win.mainloop()