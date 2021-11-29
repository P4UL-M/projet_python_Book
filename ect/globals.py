import sys
from pathlib import Path

PATH = Path("/".join(sys.argv[0].split("/")[:-1]) or "\\".join(sys.argv[0].split("\\")[:-1])).cwd() / "data"


import tkinter as tk

WINDOW = tk.Tk()
WINDOW.title("Welcome to our Book app")
WINDOW.geometry('800x600')

STYLES = {
    '1':("Sci-Fi","blue"),
    '2':("Biography","grey"),
    '3':("Horror","black"),
    '4':("Romance","red"),
    '5':("Fable","yellow"),
    '6':("History","green"),
    '7':("Comedy","pink"),
    '8':("Fantasy","orange"),
    '9':("Thriller","violet")
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