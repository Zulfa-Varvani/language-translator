import tkinter as tk
from tkinter import *
import tkinter
import pandas as pd

screen = tkinter.Tk()
buttons = ['q','w', 'e', 'r', 't', 'y', 'u','i', 
'o', 'p', 'a', 's', 'd', 'f', 'g','h',
'j', 'k' , 'l', 'z', 'x', 'c','v','b',
'n','m','ê','é', 'â' ,'û' ,'BACK','SPACE']

db = pd.read_csv('database.csv',encoding='latin-1')

#DEFINE KEYBoard
def select(value):
    if value == "BACK":
        entry.delete(len(entry.get())-1,tkinter.END)
    elif value == "SPACE":
        entry.insert(tkinter.END, ' ')
    else :
        entry.insert(tkinter.END,value)
   
def HosoPop():
    varRow = 30
    varColumn = 0
    keyboard_letter = []
    #Create button 
    for count in range (0, len(buttons)):
        command = lambda x=buttons[count]: select(x)
        button_insert= tkinter.Button(screen,text= buttons[count],width=6, bg="#3c4987", fg="#ffffff", activebackground = "#ffffff", activeforeground="#3c4987", relief='raised', padx=1, pady=1, bd=1,command=command)
        keyboard_letter.append(button_insert) 

    #Place button on grid system
    for count in range (0, 10):
        keyboard_letter[count].grid(row=varRow,column=varColumn, columnspan= 2, sticky=EW) 
        varColumn +=2
    varRow +=1
    varColumn =1
    for count in range (10, 19):
        keyboard_letter[count].grid(row=varRow,column=varColumn, columnspan= 2, sticky=EW) 
        varColumn +=2
    varRow +=1
    varColumn =2
    for count in range (19, 26):
        keyboard_letter[count].grid(row=varRow,column=varColumn, columnspan= 2, sticky=EW) 
        varColumn +=2
    varRow +=1
    varColumn =3
    for count in range (26, len(buttons)):
        keyboard_letter[count].grid(row=varRow,column=varColumn, columnspan= 2, sticky=EW) 
        varColumn +=2

def clear_widget_text():
    Label(screen, text="\t\t\t\t\t\t\t\t").grid(row=4, column=2, columnspan= 30)

def sub_val():
    word = entry.get()
    clear_widget_text()
    english = db[db.isin([word]).any(axis=1)]['English'].iloc[0]
    cree = db[db.isin([word]).any(axis=1)]['Cree'].iloc[0]
    ojib = db[db.isin([word]).any(axis=1)]['Ojibwe'].iloc[0]
    mont = db[db.isin([word]).any(axis=1)]['Montagnais'].iloc[0]
    e = Label(screen, text=english).grid(row=4, column=4+2*1, columnspan=2)
    c = Label(screen, text=cree).grid(row=4, column=4+2*2, columnspan=2)
    o = Label(screen, text=ojib).grid(row=4, column=4+2*3, columnspan=2)
    m = Label(screen, text=mont).grid(row=4, column=4+2*4, columnspan=2)

def PressKeyboard_Enter(event):
    sub_val()

# KEYBOARD
row_= 29
screen.title("Language Translator")
query = StringVar()
button1 = Button(screen,text='Translate!', command=sub_val).grid(row=row_,column=14, columnspan= 2)

screen.bind("<Return>", PressKeyboard_Enter)
HosoPop()

# MAIN
_row_main=0
heading=Label(screen, text="Indigenous Language Translator").grid(row=_row_main, column=2, columnspan= 30)
heading=Label(screen, text="========================================= ").grid(row=_row_main+1, column=2, columnspan= 30)
heading=Label(screen, text="English\tCree\tOjibway\t  Montagnais").grid(row=_row_main+2, column=2, columnspan= 30)
heading=Label(screen, text="========================================= ").grid(row=_row_main+3, column=2, columnspan= 30)

entry = Entry(screen,width=50)
entry.grid(row=row_,columnspan=15,pady=20)

#add words

#do the translation
screen.mainloop()