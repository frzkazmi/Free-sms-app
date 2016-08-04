# -*- coding: utf-8 -*-
import way2test as s


from Tkinter import *
from tkFont import Font

root = Tk()
root.geometry("400x300")
root.title("Way2SmSApp")
root.config()
mainFrame = Frame(root)
mainFrame.grid()
v1=IntVar()
v2=IntVar()
msg=StringVar()
L1 = Label(mainFrame,text=" Your userid:",fg="blue",pady=2)
L2 = Label(mainFrame,text="Password:",fg="blue",pady=6)
L3 = Label(mainFrame,text="Destination number:",fg="blue",pady=6)
L4 = Label(mainFrame,text="Message:",fg="blue",pady=6)

E1 = Entry(mainFrame)
E2 = Entry(mainFrame, show="*")
E3 = Entry(mainFrame)
entryFrame = Frame(mainFrame, width=100, height=20)
entryFrame.grid(row=3, column=1,sticky=S)


# allow the column inside the entryFrame to grow    
entryFrame.columnconfigure(0, weight=6)  

# By default the frame will shrink to whatever is inside of it and 
# ignore width & height. We change that:
entryFrame.grid_propagate(False)
E4 = Text(mainFrame,height=7, width=45,pady=6)
b = Button(mainFrame, text="LOGIN", height=-2, bg="white", fg="black", pady=3, command=lambda: s.login(E1.get(), E2.get()),width=15)
b1 = Button(mainFrame,text="SEND SMS", bg="white", fg="black",pady=5, command=lambda: s.send_sms(E3.get(), E4.get("1.0",END)),width=15)

L1.grid(row = 0,column = 0,sticky=S,padx=12)
L2.grid(row = 1,column = 0,sticky=S)
L3.grid(row = 2,column = 0,sticky=S)
L4.grid(row = 3,column = 0,sticky=S)

E1.grid(row = 0,column = 1,sticky=S)
E2.grid(row = 1,column = 1,sticky=S)
E3.grid(row = 2,column = 1,sticky=S)
E4.grid(row = 3,column = 1,sticky=S)
E4.columnconfigure(0, weight=100)
b.grid(columnspan = 6,column=0,pady=5)
b1.grid(columnspan=6)
L5 = Label(mainFrame,text="WAY2SMS APP CREATED BY JOUN",fg="red", font=4,justify=CENTER)
L6 = Label(mainFrame,text="All Rights Reserved © ",fg="red",font=0,justify=RIGHT)
L5.grid(row = 7,column=1,columnspan = 7,pady=1,ipady = "6",sticky=E)
L6.grid(row = 8,column=1,columnspan = 5)


root.mainloop()


