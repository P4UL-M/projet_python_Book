import sys
from pathlib import Path

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

def Recursive_Binding(parent,event,func):
    parent.bind(event,func)
    for child in parent.winfo_children():
        Recursive_Binding(child,event,func)