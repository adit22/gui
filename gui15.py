from tkinter import *
wind=Tk()
wind.resizable(width=FALSE,height=FALSE)
wind.title("message box")
msg=''' life can't be always about solving problem,there have to  be things  for which you are glad to wake up in the morning'''

var1=Message(wind,text=msg,bg="black",fg="red",anchor='ne',justify='center',bd=12,font="ariel 40 bold",relief='groove',takefocus="True")
var1.pack()
wind.mainloop()
