from db import *
import tkinter as tk
from tkinter import *
from translate import *
from keyboard import *

screen=Tk() #Creating a GUI window
screen.geometry("600x400")
screen.title("REC2021")

def engToCree():
    outputWindow=Toplevel(screen)
    outputWindow.title("Result")
    outputWindow.geometry("600x400")
    heading=Label(outputWindow, text="English to Cree").place(x=200, y=10)
    w = Label(outputWindow, text="Word: "+new_var)
    w.place(x=300,y=100)
    toLang(outputWindow,extract_word(new_var), cree)
def creeToEng():
    outputWindow=Toplevel(screen)
    outputWindow.title("Result")
    outputWindow.geometry("600x400")
    heading=Label(outputWindow, text="Cree to English").place(x=200, y=10)
    w = Label(outputWindow, text="Word: "+new_var)
    w.place(x=300,y=100)
    toEng(outputWindow,extract_word(new_var), cree)
def engToOj():
    outputWindow=Toplevel(screen)
    outputWindow.title("Result")
    outputWindow.geometry("600x400")
    heading=Label(outputWindow, text="English to Ojibway").place(x=200, y=10)
    w = Label(outputWindow, text="Word: "+new_var)
    w.place(x=300,y=100)
    toLang(outputWindow,extract_word(new_var), ojibwe)
def ojToEng():
    outputWindow=Toplevel(screen)
    outputWindow.title("Result")
    outputWindow.geometry("600x400")
    heading=Label(outputWindow, text="Ijibway to English").place(x=200, y=10)
    w = Label(outputWindow, text="Word: "+new_var)
    w.place(x=300,y=100)
    toEng(outputWindow,extract_word(new_var), ojibwe)
def engToMon():
    outputWindow=Toplevel(screen)
    outputWindow.title("Result")
    outputWindow.geometry("600x400")
    heading=Label(outputWindow, text="English to Montagnais").place(x=200, y=10)
    w = Label(outputWindow, text="Word: "+new_var)
    w.place(x=300,y=100)
    toLang(outputWindow,extract_word(new_var), mont)
def monToEng():
    outputWindow=Toplevel(screen)
    outputWindow.title("Result")
    outputWindow.geometry("600x400")
    heading=Label(outputWindow, text="Montagnais to English").place(x=200, y=10)
    w = Label(outputWindow, text="Word: "+new_var)
    w.place(x=300,y=100)
    toEng(outputWindow,extract_word(new_var), mont)

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

heading=Label(screen, text="Indigenous Language Translator").place(x=200, y=10)
headingEnglish=Label(screen, text="Word is:").place(x=150, y=50)
varLabel = Label(screen, text=new_var).place(x=150, y = 80)
    
englishToCree=Button(screen, text="Translate English to Cree", height=2, width=20, command=engToCree).place(x=100, y=145)
creeToEnglish=Button(screen, text="Translate Cree to English", height=2, width=20, command=creeToEng).place(x=300, y=145)
englishToOjibway=Button(screen, text="Translate English to Ojibway", height=2, width=20, command=engToOj).place(x=100, y=200)
ojibwayToEnglish=Button(screen, text="Translate Ojibway to English", height=2, width=20, command=ojToEng).place(x=300, y=200)
englishToMontagnais=Button(screen, text="Translate English to Montagnais", height=2, width=25, command=engToMon).place(x=65, y=255)
montagnaisToEnglish=Button(screen, text="Translate Montagnais to English", height=2, width=25, command=monToEng).place(x=300, y=255)
addWords=Button(screen, text="ADD", height=2, width=20, command=addWordWindow).place(x=200, y=310)

mainloop()