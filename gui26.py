from tkinter import *
wind=Tk()

wind.title("rectangle")

x=400
y=300
var2=Canvas(wind,width=x,height=y)
var2.pack()
var2.create_rectangle(250,20,350,80,fill="#476042")
var1=Label(wind,text="rectange",font="ariel 10 bold")
var1.pack()

wind.mainloop()
