from tkinter import *
window=Tk()
#window is object of class Tk
window.geometry("300x300")
#we can set geometry of the window
Label(window,text="hello",font="ariel 40 bold").pack()
#label is used to display message
window.mainloop()
