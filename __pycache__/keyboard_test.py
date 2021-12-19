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
    varRow = 3
    varColumn = 0
    keyboard_letter = []
    #Create button 
    for count in range (0, len(buttons)):
        command = lambda x=buttons[count]: select(x)
        button_insert= tkinter.Button(kb,text= buttons[count],width=6, bg="#3c4987", fg="#ffffff", activebackground = "#ffffff", activeforeground="#3c4987", relief='raised', padx=1, pady=1, bd=1,command=command)
        keyboard_letter.append(button_insert) 

    #Place button on grid system
    for count in range (0, 10):
        keyboard_letter[count].grid(row=varRow,column=varColumn, columnspan= 2) 
        varColumn +=2
    varRow +=1
    varColumn =1
    for count in range (10, 19):
        keyboard_letter[count].grid(row=varRow,column=varColumn, columnspan= 2) 
        varColumn +=2
    varRow +=1
    varColumn =2
    for count in range (19, 26):
        keyboard_letter[count].grid(row=varRow,column=varColumn, columnspan= 2) 
        varColumn +=2
    varRow +=1
    varColumn =3
    for count in range (26, len(buttons)):
        keyboard_letter[count].grid(row=varRow,column=varColumn, columnspan= 2) 
        varColumn +=2

def sub_val():
    global new_var
    new_var = entry.get()
    #new_var = StringVar(value = entry.get())
    kb.destroy()

def PressKeyboard_Enter(event):
    sub_val()

kb.title("keyboard")
#kb.resizable(0,0)
query = StringVar()
button1 = Button(kb,text='Enter!', command=sub_val).grid(row=1,column=14, columnspan= 2)

kb.bind("<Return>", PressKeyboard_Enter)
HosoPop()

entry = Entry(kb,width=50)
entry.grid(row=1,columnspan=15,pady=20)
# entry.pack()



kb.mainloop()