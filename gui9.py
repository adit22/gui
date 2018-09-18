from tkinter import *
window=Tk()
#window is object of class Tk
window.geometry("600x600")
window.title("my_gui")
#we can set geometry of the window
var=PhotoImage(file="hello.png")
#adding image to window
a="""this is a image"""
var1=Label(window,image=var,text=a,compound=CENTER)
var1.pack()
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
