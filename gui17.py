from tkinter import *
wind=Tk()
wind.geometry("400x400")
wind.title("message box")
def msg():

    
    var1=Message(wind,text=var4.get(),bg="black",fg="red",anchor='ne',justify='center',bd=12,font="ariel 40 bold")
    var1.pack()


var4=Entry(wind)
var4.pack()
var2=Button(wind,text="click here",font="ariel 20 bold",fg="black",bg="red",command=msg)
var2.pack()
    
    
wind.mainloop()
