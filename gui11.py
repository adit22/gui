from tkinter import *
m=0
def counter(var2):
    def count():
        global m
        
        m+=1
        var2.config(text=str(m))
        var2.after(1000,count)
    count()

def fun():
    Label(text="thankyu").pack()
    var1.destroy()
var1=Tk()
var1.geometry("800x600")
var1.title("stop-watch")
varr=Label(var1,text="count-time",font="ariel 40 bold",fg="green")
varr.pack()
var2=Label(var1,text="count-time",font="ariel 40 bold",fg="red")
var2.pack()
counter(var2)
var3=Button(var1,text="stop",font="ariel  10 bold",command=fun)
var3.pack()
    
var1.mainloop()
