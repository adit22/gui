from tkinter import *
wind=Tk()
var1=Label(wind,text="canvas and line",font="ariel 10 bold")
var1.pack()
x=800
y=600
var2=Canvas(wind,width=x,height=y)
var2.pack()
x1=int(x/2)
y1=int(y/2)
var2.create_line(80,80,80,y1,fill="#476042")
var2.create_line(80,80,x1,80,fill="#476042")
var2.create_line(x1,80,x1,y1,fill="#476042")
var2.create_line(x1,y1,80,y1,fill="#476042")
var2.create_line(80,y1,x1,80,fill="#476042")
var2.create_line(80,80,x1,y1,fill="#476042")
wind.mainloop()
