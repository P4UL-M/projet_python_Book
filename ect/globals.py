import sys
from pathlib import Path

PATH = Path("/".join(sys.argv[0].split("/")[:-1]) or "\\".join(sys.argv[0].split("\\")[:-1])).cwd() / "data"


import tkinter as tk

WINDOW = tk.Tk()
WINDOW.title("Welcome to our Book app")
WINDOW.geometry('800x600')