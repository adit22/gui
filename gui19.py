from tkinter import *
wind=Tk()
def show():
    Label(wind,text=v.get(),font=("ariel 20 bold"),bg="black",fg="red").pack()
var1=Label(wind,text="select your preference",font="ariel 20 bold",bg="black",fg="red")
var1.pack()
pref_lang=[("c",0),("c++",1),("python",2),("brainfk",3)]
v=IntVar()
for val,lang in enumerate(pref_lang):
    var2=Radiobutton(wind,text=lang[0],variable=v,value=val,command=show)
    var2.pack()

    
wind.mainloop()
