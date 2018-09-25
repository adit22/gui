from tkinter import *
windo=Tk()
windo.geometry("600x800")
windo.title("radiobutton_test")
def city():
    if(varr.get()==1):
        Label(windo,text="vns",font="ariel 20 bold").grid(row=5,column=4)
    elif(varr.get()==2):
        Label(windo,text="patna",font="ariel 20 bold").grid(row=5,column=4)
    elif(varr.get()==3):
        Label(windo,text="gngtk",font="ariel 20 bold").grid(row=5,column=4)
    elif(varr.get()==4):
        Label(windo,text="drj",font="ariel 20 bold").grid(row=5,column=4)
    else:
        Label(wind,text="None",font="ariel 20 bold").grid(row=5,column=4)

var1=Label(windo,text='radiobutton',font="ariel 20 bold")
var1.grid(row=2,column=2)
varr=IntVar()
var2=Radiobutton(windo,text="varanasi",variable=varr,value=1)
var2.grid(row=4,column=3)
var3=Radiobutton(windo,text="patna",variable=varr,value=2)
var3.grid(row=4,column=4)
var4=Radiobutton(windo,text="gangtok",variable=varr,value=3)
var4.grid(row=4,column=5)
var5=Radiobutton(windo,text="darjeeling",variable=varr,value=4)
var5.grid(row=4,column=6)
var6=Button(windo,text="submit here",font="ariel 20 bold",command=city)
var6.grid(row=6,column=4)
windo.mainloop()
