import re
import enchant
import tkinter as tk
from tkinter import *
from db import *

def extract_word(text):
    regex = r"(\w|\s)*"
    matches = re.finditer(regex, text, re.DOTALL)
    newstr = ''
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
        newstr = newstr + match.group()
    return newstr

def toEng(win, word, d):
    if word in d:
        return d[word]
def toLang(win,word, d):
    new = ''.join([k for k, v in d.items() if v == word])
    return new



def FindtypeWord(word):
    if word in cree:
        return "cree"
    if word in ojibwe:
        return "ojibwe"
    if word in mont:
        return "mont"
    d=enchant.Dict("en_US")
    if (d.check(word) == True):
        return "english"
    else:
        return "Not a language"

def wordisenglish(screen, new_var):  
    table_column_start =4
    table_row_start = 4
    table_columnspan = 2
    w = Label(screen, text=new_var)
    w.grid(row= table_row_start,column= table_column_start+table_columnspan*1,columnspan= table_columnspan)
    w = toLang(screen,extract_word(new_var), cree)
    if w == "":
        w = Label(screen, text="None")
    else:
        w = Label(screen, text=w)
    w.grid(row= table_row_start,column= table_column_start+table_columnspan*2,columnspan= table_columnspan)
    w = toLang(screen,extract_word(new_var), ojibwe)
    if w == "":
        w = Label(screen, text="None")
    else:
        w = Label(screen, text=w)
    w.grid(row= table_row_start,column= table_column_start+table_columnspan*3,columnspan= table_columnspan)
    w = toLang(screen,extract_word(new_var), mont)
    if w == "":
        w = Label(screen, text="None")
    else:
        w = Label(screen, text=w)
    w.grid(row= table_row_start,column= table_column_start+table_columnspan*4,columnspan= table_columnspan)


def wordiscree(screen, new_var):
    table_column_start =4
    table_columnspan = 2
    w = Label(screen, text=new_var)
    w.grid(row= 4,column= table_column_start+table_columnspan*2,columnspan= table_columnspan)
    w_eng = str(toEng(screen,extract_word(new_var), cree))
    w=w_eng
    if w == '':
        w = Label(screen, text="None")
    else:
        w = Label(screen, text=w)
    w.grid(row= 4,column= table_column_start+table_columnspan*1,columnspan= table_columnspan)
    w = toLang(screen,extract_word(w_eng), ojibwe)
    if w == "":
        w = Label(screen, text="None")
    else:
        w = Label(screen, text=w)
    w.grid(row= 4,column= table_column_start+table_columnspan*3,columnspan= table_columnspan)

    w = toLang(screen,extract_word(w_eng), mont)
    if w == "":
        w = Label(screen, text="None")
    else:
        w = Label(screen, text=w)
    w.grid(row= 4,column= table_column_start+table_columnspan*4,columnspan= table_columnspan)

def wordisojibwe(screen, new_var):
    table_column_start =4
    table_columnspan = 2
    w = Label(screen, text=new_var)
    w.grid(row= 4,column= table_column_start+table_columnspan*3,columnspan= table_columnspan)
    w_eng = str(toEng(screen,extract_word(new_var), ojibwe))
    w=w_eng
    if w == '':
        w = Label(screen, text="None")
    else:
        w = Label(screen, text=w)
    w.grid(row= 4,column= table_column_start+table_columnspan*1,columnspan= table_columnspan)
    w = toLang(screen,extract_word(w_eng), cree)
    if w == "":
        w = Label(screen, text="None")
    else:
        w = Label(screen, text=w)
    w.grid(row= 4,column= table_column_start+table_columnspan*2,columnspan= table_columnspan)
    w = toLang(screen,extract_word(w_eng), mont)
    if w == "":
        w = Label(screen, text="None")
    else:
        w = Label(screen, text=w)
    w.grid(row= 4,column= table_column_start+table_columnspan*4,columnspan= table_columnspan)

def wordismont(screen, new_var):
    table_column_start =4
    table_columnspan = 2
    w = Label(screen, text=new_var)
    w.grid(row= 4,column= table_column_start+table_columnspan*4,columnspan= table_columnspan)
    w_eng = str(toEng(screen,extract_word(new_var), mont))
    w=w_eng
    if w == '':
        w = Label(screen, text="None")
    else:
        w = Label(screen, text=w)
    w.grid(row= 4,column= table_column_start+table_columnspan*1,columnspan= table_columnspan)
    w = toLang(screen,extract_word(w_eng), cree)
    if w == "":
        w = Label(screen, text="None")
    else:
        w = Label(screen, text=w)
    w.grid(row= 4,column= table_column_start+table_columnspan*2,columnspan= table_columnspan)
    w = toLang(screen,extract_word(w_eng), ojibwe)
    if w == "":
        w = Label(screen, text="None")
    else:
        w = Label(screen, text=w)
    w.grid(row= 4,column= table_column_start+table_columnspan*3,columnspan= table_columnspan)
