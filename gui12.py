from tkinter import *
def add():
    Label(text=str(int(var3.get())+int(var5.get()))).pack()
    

var1=Tk()
var1.geometry("800x600")
var1.title("adding two number")
var2=Label(var1,text="enter first value",font="ariel 40 bold")
var2.pack()
var3=Entry(var2)
var3.pack()
var4=Label(var1,text="enter second value",font="ariel 40 bold")
var4.pack()
var5=Entry(var4)
var5.pack()
var6=Button(var1,text="add",command=add)
var6.pack()
var1.mainloop()
