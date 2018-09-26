from tkinter import *
wind=Tk()
def show():
    if(v1.get()==1):
        Label(wind,text="c",font=("ariel 20 bold"),bg="black",fg="red").pack()
    if(v2.get()==2):
        Label(wind,text="c++",font=("ariel 20 bold"),bg="black",fg="red").pack()
    if(v3.get()==3):
        Label(wind,text="python",font=("ariel 20 bold"),bg="black",fg="red").pack()
    if(v4.get()==4):
        Label(wind,text="brainfk",font=("ariel 20 bold"),bg="black",fg="red").pack()
var1=Label(wind,text="check your pref.",bg="black",fg="red")
var1.pack()
v1=IntVar()
var2=Checkbutton(wind,text="c",variable=v1,onvalue=1,command=show)
var2.pack()
v2=IntVar()
var3=Checkbutton(wind,text="c++",variable=v2,onvalue=2,command=show)
var3.pack()
v3=IntVar()
var4=Checkbutton(wind,text="python",variable=v3,onvalue=3,command=show)
var4.pack()
v4=IntVar()
var5=Checkbutton(wind,text="brainfk",variable=v4,onvalue=4,command=show)
var5.pack()



wind.mainloop()
