from ect.globals import AGES, WINDOW,STYLES,GENDER
import tkinter as tk
import tkinter.ttk as ttk
from lib.users_functions import *

def set_user(name):
    user = get_reader(name)

    tab:tk.Frame = WINDOW.nametowidget('.!notebook').nametowidget('profile')
    tab.nametowidget("pseudo")["text"] = user["name"]
    tab.nametowidget("gender")["text"] = GENDER[user["gender"]]
    tab.nametowidget("age")["text"] = AGES[user["age"]]
    tab.nametowidget("favorite")["text"] = STYLES[user["favorite"]][0]
    tab.nametowidget("pdp")["bg"] = STYLES[user["favorite"]][1]
    
    WINDOW.nametowidget('.!notebook').pack(fill="both",expand=1)

def user_portal(on_close = None):
    win = tk.Toplevel(WINDOW)
    win.geometry("343x122")
    
    win.title("Connection portal")
    win.focus_force()
    
    # must overide the normal app because the user can launch other function that will looping for ever
    # no pretty way to do it by removing all elt of Part3 so we remove all
    WINDOW.nametowidget('.!notebook').pack_forget()

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
    name_widget.focus()

    def handledata(e=None):
        name = name_widget.get()
        if name:
            set_user(name)
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
    win.geometry("800x250")
    
    win.title("Edit profile")
    win.focus_force()

    main = ttk.Frame(win)
    main.pack(fill="both",expand=1)
    old_name = WINDOW.nametowidget('.!notebook').nametowidget('profile').nametowidget('pseudo')['text']
    user = get_reader(old_name)

    #region name widget
    name_widget = ttk.Label(main,name="pseudo", text="Pseudo :",padding=15)
    name_widget.grid(row=0,column=0,sticky="nw")

    #name entry
    name_entry = ttk.Entry(main)
    name_entry.grid(column=1,row=0)
    name_entry.insert(-1, user["name"])

    #endregion

    #region gender widget
    gender_widget = ttk.Label(main,name="gender", text="Gender :",padding=15)
    gender_widget.grid(row=1,column=0,sticky="nw")
    
    #gender entry
    rad_gender = dict()
    gender_value = tk.StringVar()
    rad_gender["1"] = ttk.Radiobutton(main,text='Man',variable=gender_value, value="1",command=gender_value.get);rad_gender["1"].grid(column=1, row=1)
    rad_gender["2"] = ttk.Radiobutton(main,text='Woman',variable=gender_value, value="2",command=gender_value.get);rad_gender["2"].grid(column=2,row=1)
    rad_gender["3"] = ttk.Radiobutton(main,text='No Matter What',variable=gender_value, value="3",command=gender_value.get);rad_gender["3"].grid(column=3,row=1)

    rad_gender[user["gender"]].invoke()
    #endregion

    #region age widget
    age_widget = ttk.Label(main,name="age",text="Age :",padding=15)
    age_widget.grid(row=2,column=0,sticky="nw")
    
    #age entry
    rad_age = dict()
    age_value = tk.StringVar()
    rad_age["1"] = ttk.Radiobutton(main,text='>18 years old',variable=age_value, value="1",command=age_value.get);rad_age["1"].grid(column=1, row=2)
    rad_age["2"] = ttk.Radiobutton(main,text='Between 18 and 25 years old',variable=age_value, value="2",command=age_value.get);rad_age["2"].grid(column=2,row=2)
    rad_age["3"] = ttk.Radiobutton(main,text='<25 years old',variable=age_value, value="3",command=age_value.get);rad_age["3"].grid(column=3,row=2)

    rad_age[user["age"]].invoke()
    #endregion

    #region favorite widget
    favorite_widget = ttk.Label(main,name="favorite",text="Favorite style :",padding=15)
    favorite_widget.grid(row=3,column=0,sticky="nw")

    #favorite entry
    favorite_combo = ttk.Combobox(main)
    favorite_combo['values']= ("Sci-Fi", "Biography", "Horror", "Romance", "Fable", "History","Comedy","Fantasy","Thriller")
    favorite_combo.current(int(user["favorite"])-1)
    favorite_combo.grid(column=1, row=3)
    #endregion

    def save_data():
        new_name = name_entry.get()
        new_gender = gender_value.get()
        new_age =age_value.get()
        new_favorite = str(favorite_combo['values'].index(favorite_combo.get()) + 1)
        update_reader(old_name=old_name,name=new_name,gender=new_gender,age=new_age,favorite=new_favorite)
        set_user(new_name)
        win.destroy()

    btn_save = ttk.Button(main,text="  Save  ",command=save_data)
    btn_save.grid(column=1,row=4,columnspan=2)