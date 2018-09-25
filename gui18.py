from tkinter import *
wind=Tk()
wind.geometry("600x800")
wind.title("my window")
wind.resizable(width=FALSE,height=FALSE)
def one():
    vr1.set("button1 was clicked")
    var4=Label(wind,text=vr1)
    var4.grid(row=4,column=4)
    
def two():
    vr1.set("button2 was clicked")
    var5=Label(wind,text=vr1)
    var5.grid(row=5,column=4)
    
vr1=StringVar()
vr1.set("click any button")
var3=Label(wind,text=vr1)
var3.grid(row=1,column=2)

var1=Button(wind,text="button1",bg="black",fg="red",command=one)
var1.grid(row=2,column=2)
var2=Button(wind,text="button2",bg="black",fg="red",command=two)
var2.grid(row=3,column=2)

wind.mainloop()
