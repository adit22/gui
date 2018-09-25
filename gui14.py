from tkinter import *
wind=Tk()
wind.geometry("600x800")
wind.title("checkbox")
def city():
    if(vr1.get()==1):
        Label(wind,text="vns",font="ariel 20 bold").grid(row=5,column=4)
    if(vr2.get()==2):
        Label(wind,text="patna",font="ariel 20 bold").grid(row=6,column=4)
    if(vr3.get()==3):
        Label(wind,text="gngtk",font="ariel 20 bold").grid(row=7,column=4)
    if(vr4.get()==4):
        Label(wind,text="drj",font="ariel 20 bold").grid(row=8,column=4)
    
    
    
var1=Label(wind,text="checkbox",font="ariel 20 bold")
var1.grid(row=0,column=0)
vr1=IntVar()
var2=Checkbutton(wind,text="vns",variable=vr1,onvalue=1)
var2.grid(row=1,column=2)
vr2=IntVar()
var3=Checkbutton(wind,text="ptn",variable=vr2,onvalue=2)
var3.grid(row=1,column=3)
vr3=IntVar()
var4=Checkbutton(wind,text="gngtk",variable=vr3,onvalue=3)
var4.grid(row=1,column=4)
vr4=IntVar()
var5=Checkbutton(wind,text="drj",variable=vr4,onvalue=4)
var5.grid(row=1,column=5)
var6=Button(wind,text="submit here",font="ariel 20 bold",command=city)
var6.grid(row=2,column=4)

wind.mainloop()
