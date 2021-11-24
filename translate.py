import re
import tkinter as tk
from tkinter import *

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
        w = Label(win, text="Translated: "+d[word])
        w.place(x=300,y=250)
def toLang(win,word, d):
    new = ''.join([k for k, v in d.items() if v == word])
    w = Label(win, text="Translated: "+new)
    w.place(x=300,y=250)