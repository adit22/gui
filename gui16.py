from tkinter import *
wind=Tk()
wind.geometry("400x400")
wind.title("message box")

def msg():
    msg=''' life can't be always about solving problem,there have to  be things  for which you are glad to wake up in the morning'''
    var1=Message(wind,text=msg,bg="black",fg="red",anchor='ne',justify='center',bd=12,font="ariel 40 bold")
    var1.pack()


var2=Button(wind,text="click to see quote",font="ariel 20 bold",fg="black",bg="red",command=msg)
var2.pack()

    
wind.mainloop()
