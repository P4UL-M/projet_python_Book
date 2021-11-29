from ect.globals import AGES, WINDOW,STYLES,GENDER
import tkinter as tk
import tkinter.ttk as ttk
from lib.users_functions import *

def get_connection(on_close = None):
    win = tk.Toplevel(WINDOW)
    win.geometry("343x122")
    
    win.title("Connection portal")
    win.focus_force()

    main = ttk.Frame(win)
    main.pack(fill="both",expand=1)

    def on_focus_out(event):
        if event.widget == win:
            win.focus_force()

    def on_closing():
        if on_close != None:
            on_close()
        win.destroy()

    center = ttk.Frame(main)
    center.place(relx=0.5, rely=0.5, anchor="center")
    name_widget = ttk.Entry(center)
    name_widget.grid(column=0,row=0)

    def handledata(e=None):
        name = name_widget.get()
        if name:
            user = get_reader(name)

            tab:tk.Frame = WINDOW.nametowidget('.!notebook').nametowidget('profile')
            test = tk.Label(tab,text=user["name"]).pack()
            test_2 = tk.Label(tab,text=GENDER[user["gender"]]).pack()
            test_3 = tk.Label(tab,text=AGES[user["age"]]).pack()
            test_4 = tk.Label(tab,text=STYLES[user["favorite"]][0],background=STYLES[user["favorite"]][1]).pack()

            win.destroy()

    btn = ttk.Button(center,text="Connect",command=handledata)
    btn.grid(column=0,row=1,sticky="we")

    name_widget.bind("<Return>",handledata)
    name_widget.bind("<")
    win.bind("<FocusOut>", on_focus_out)
    win.protocol("WM_DELETE_WINDOW", on_closing)