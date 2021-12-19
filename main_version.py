
from db import *
import tkinter as tk
from tkinter import *
from translate_copy import *
import tkinter

screen = tkinter.Tk()
buttons = [
'q','w', 'e', 'r', 't', 'y', 'u','i', 
'o', 'p', 'a', 's', 'd', 'f', 'g','h',
'j', 'k' , 'l', 'z', 'x', 'c','v','b',
'n','m','ê','é', 'â' ,'û' ,'BACK','SPACE'
]


#DEFINE KEYBoard ==================================================================================
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
    # screen.destroy()
    wordisenglish(screen, new_var)

def PressKeyboard_Enter(event):
    sub_val()

#DEFINE main ======================================================================



def addWordWindow():
    addWordWindow=Toplevel(screen)
    addWordWindow.title("Add new word")
    addWordWindow.geometry("600x400")
    heading=Label(addWordWindow,text="Add new word").place(x=250, y=20)
    headingEnglish=Label(addWordWindow, text="English").place(x=150, y=75)
    eEnglish=Entry(addWordWindow, width=25)
    eEnglish.place(x=200, y=75)
    englishWord=eEnglish.get()#Takes the english input, puts into variable
    headingIndigenous =Label(addWordWindow, text="Indigenous Language").place(x=75, y=100)
    eIndigenous =Entry(addWordWindow, width=25)
    eIndigenous.place(x=200, y=100)
    indigenousWord=eIndigenous.get()#input -> variable
    def addEnglishToCree():
        cree['indigenousWord']='englishWord'
        print("Updated!")
    def addEnglishtoOjibway():
        ojibwe[indigenousWord]=englishWord
    def addEnglishtoMontagnais():
        mont[indigenousWord]=englishWord
    englishToCree=Button(addWordWindow, text="English & Cree", height=2, width=20, command=addEnglishToCree).place(x=200, y=170)
    englishToOjibway=Button(addWordWindow, text="English & Ojibway", height=2, width=20, command=addEnglishtoOjibway).place(x=200, y=235)
    englishToMontagnais=Button(addWordWindow, text="English & Montagnais", height=2, width=20, command=addEnglishtoMontagnais).place(x=200, y=300)



# KEYBOARD==================================================================================
row_= 29
screen.title("keyboard")
#kb.resizable(0,0)
query = StringVar()
button1 = Button(screen,text='Enter!', command=sub_val).grid(row=row_,column=14, columnspan= 2)

screen.bind("<Return>", PressKeyboard_Enter)
HosoPop()

entry = Entry(screen,width=50)
entry.grid(row=row_,columnspan=15,pady=20)
# entry.pack()

# MAIN ===============================================================
_row_main=0
heading=Label(screen, text="Indigenous Language Translator").grid(row=_row_main, column=2, columnspan= 30)
heading=Label(screen, text="========================================= ").grid(row=_row_main+1, column=2, columnspan= 30)
heading=Label(screen, text="English        Cree       Ojibway       Montagnais   ").grid(row=_row_main+2, column=2, columnspan= 30)
heading=Label(screen, text="========================================= ").grid(row=_row_main+3, column=2, columnspan= 30)


#take the word find if it is which language 
#exctract(new_var)


#do the translation
screen.mainloop()