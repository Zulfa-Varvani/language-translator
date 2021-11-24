from tkinter import *

import tkinter

kb = tkinter.Tk()
buttons = [
'q','w', 'e', 'r', 't', 'y', 'u','i', 
'o', 'p', 'a', 's', 'd', 'f', 'g','h',
'j', 'k' , 'l', 'z', 'x', 'c','v','b',
'n','m','ê','é', 'â' ,'û' ,'BACK','SPACE'
]

def select(value):
    if value == "BACK":
        entry.delete(len(entry.get())-1,tkinter.END)
    elif value == "SPACE":
        entry.insert(tkinter.END, ' ')
    else :
        entry.insert(tkinter.END,value)

def HosoPop():
    varRow = 2
    varColumn = 0
    for button in buttons:
        command = lambda x=button: select(x)
        if button == "SPACE" or button == "BACK" or "ENTER":
            tkinter.Button(kb,text= button,width=6, bg="#3c4987", fg="#ffffff",
                activebackground = "#ffffff", activeforeground="#3c4987", relief='raised', padx=1,
                pady=1, bd=1,command=command).grid(row=varRow,column=varColumn)
        else:
            tkinter.Button(kb,text= button,width=4, bg="#3c4987", fg="#ffffff",
                activebackground = "#ffffff", activeforeground="#3c4987", relief='raised', padx=1,
                pady=1, bd=1,command=command).grid(row=varRow,column=varColumn)
        varColumn +=1

        if varColumn > 14 and varRow == 2:
            varColumn = 0
            varRow+=1
        if varColumn > 14 and varRow == 3:
            varColumn = 0
            varRow+=1
        if varColumn > 14 and varRow == 4:
            varColumn = 0
            varRow+=1

def sub_val():
    global new_var
    new_var = entry.get()
    #new_var = StringVar(value = entry.get())
    kb.destroy()

kb.title("keyboard")
kb.resizable(0,0)
query = StringVar()
button1 = Button(kb,text='Enter!', command=sub_val).grid(row=0,columnspan=15)

entry = Entry(kb,width=50)
entry.grid(row=1,columnspan=15)
# entry.pack()

entry.bind("<Button-1>", lambda e: HosoPop())

kb.mainloop()