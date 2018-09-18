from tkinter import *
window=Tk()
#window is object of class Tk
window.geometry("300x300")
window.title("my_gui")
#we can set geometry of the window

var1=Label(window,text="welcome",font="ariel 40 bold",padx=20,justify=RIGHT)
var1.pack(side="right")
#label is used to display message
#if label is assinged to a variable , then use pack with that variable
var2=Entry(window)
var2.pack()
#entry is used to receive input from user

def fun():
    Label(window,text="hello "+var2.get(),font="ariel 40 bold").pack()



var3=Button(window,text="click here",bg="red",command=fun)
var3.pack()
#button is used here
window.mainloop()
