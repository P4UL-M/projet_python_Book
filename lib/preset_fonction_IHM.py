from tkinter.constants import W
from ect.globals import AGES, WINDOW,STYLES,GENDER
import tkinter as tk
import tkinter.ttk as ttk
from lib.users_functions import *

def user_portal(on_close = None):
    win = tk.Toplevel(WINDOW)
    win.geometry("343x122")
    
    win.title("Connection portal")
    win.focus_force()
    
    # must overide the normal app because the user can launch other function that will looping for ever
    # no pretty way to do it by removing all elt of Part3 so we remove all
    WINDOW.nametowidget('.!notebook').pack_forget()
    overide = ttk.Frame(WINDOW);overide.pack(fill="both",expand=1)

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
            debug = tab.nametowidget("pseudo")
            tab.nametowidget("pseudo")["text"] = user["name"]
            tab.nametowidget("gender")["text"] = GENDER[user["gender"]]
            tab.nametowidget("age")["text"] = AGES[user["age"]]
            tab.nametowidget("favorite")["text"] = STYLES[user["favorite"]][0]
            tab.nametowidget("pdp")["bg"] = STYLES[user["favorite"]][1]
            
            WINDOW.nametowidget('.!notebook').pack(fill="both",expand=1)
            overide.pack_forget()
            
            win.destroy()

    btn = ttk.Button(center,text="Connect",command=handledata)
    btn.grid(column=0,row=1,sticky="we")

    name_widget.bind("<Return>",handledata)
    name_widget.bind("<")
    win.bind("<FocusOut>", on_focus_out)
    win.protocol("WM_DELETE_WINDOW", on_closing)

def get_user():
    tab:tk.Frame = WINDOW.nametowidget('.!notebook').nametowidget('profile')

    user = dict()

    _name:tk.Label = tab.nametowidget('pseudo')
    user = get_reader(_name['text'])
    if user: #ajouter super condition
        return user
    else:
        return False

def disconnect():
    tab:tk.Frame = WINDOW.nametowidget('.!notebook').nametowidget('profile')

    tab.nametowidget("pseudo")["text"] = ""
    tab.nametowidget("gender")["text"] = ""
    tab.nametowidget("age")["text"] = ""
    tab.nametowidget("favorite")["text"] = ""
    tab.nametowidget("pdp")["bg"] = "white"

    onglets = WINDOW.nametowidget('.!notebook')
    home = WINDOW.nametowidget('.!notebook').nametowidget('home')
    onglets.select(home); home.focus_set()

def edit_user():
    win = tk.Toplevel(WINDOW)
    win.geometry("343x122")
    
    win.title("Edit profile")
    win.focus_force()

    main = ttk.Frame(win)
    main.pack(fill="both",expand=1)