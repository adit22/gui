from tkinter import *
window=Tk()
#window is object of class Tk
window.geometry("300x300")
window.title("my_gui")
#we can set geometry of the window
var=Label(window,text="hello",font="ariel 40 bold")
var.pack()
#label is used to display message
#if label is assinged to a variable , then use pack with that variable
window.mainloop()
