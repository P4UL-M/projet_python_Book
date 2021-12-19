import sys
from pathlib import Path

"""
This file contain constant we need in every other file, to avoid circular import we use a global file (python global variables aren't global to every file)
"""

#this library allow to user / operator in path and work for every following case of every OS :
# 
# In Mac/Linux :
#  % python /user/document/projet_python_book/main.py
# ~/projet_python_book % python main.py
# 
# in Windows :
# % python \user\document\projet_python_book\main.py
# ~\projet_python_book % python main.py
# 
# run with the App.pyw
PATH = Path("/".join(sys.argv[0].split("/")[:-1]) or "\\".join(sys.argv[0].split("\\")[:-1])).absolute() / "data"


import tkinter as tk

WINDOW = tk.Tk()
WINDOW.title("Welcome to your Book app")
WINDOW.geometry('800x600')

STYLES = {
    '1':("Sci-Fi","blue","orange"),
    '2':("Biography","grey","black"),
    '3':("Horror","black","white"),
    '4':("Romance","red","black"),
    '5':("Fable","yellow","black"),
    '6':("History","green","black"),
    '7':("Comedy","pink","black"),
    '8':("Fantasy","orange","black"),
    '9':("Thriller","violet","black")
    }

GENDER = {
    "1":"Man",
    "2":"Woman",
    "3":"No Matter What"
    }

AGES = {
    "1":"<18 ans",
    "2":"Entre 18 et 25 ans",
    "3":">25 ans"
}

MATRIX = list()

def update_size(size):
    """
    this function resize the object without changing it so we don't have bug with global variable
    """
    while len(MATRIX)!=size:
        if len(MATRIX)>size:
            MATRIX.pop()
        else:
            MATRIX.append([0])
    for l in MATRIX:
        while len(l)!=size:
            if len(l)>size:
                l.pop()
            else:
                l.append([0])

def Recursive_Binding(parent,event,func):
    """
    this function bind every child of a parent recursively with an event and a fonction
    """
    parent.bind(event,func)
    for child in parent.winfo_children():
        Recursive_Binding(child,event,func)

def force_update():
    """
    this function resize the window to the same size so each config function is call and it force the update of the window
    """
    WINDOW.config(height=WINDOW.winfo_height())
