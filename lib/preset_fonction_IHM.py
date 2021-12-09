from tkinter.font import Font
from ect.globals import AGES, WINDOW,STYLES,GENDER
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from lib.preset_widget import *
from lib.users_functions import *

def set_user(name):
    user = get_reader(name)
    if not user:
        msg.showerror("USER NOT FOUND", "USER NOT FOUND !\n Check that you enter the good pseudo, else try create your account again.")
    else:
        tab:tk.Frame = WINDOW.nametowidget('.!notebook').nametowidget('profile')
        tab.nametowidget("pseudo")["text"] = user["name"]
        tab.nametowidget("gender")["text"] = GENDER[user["gender"]]
        tab.nametowidget("age")["text"] = AGES[user["age"]]
        tab.nametowidget("favorite")["text"] = STYLES[user["favorite"]][0]
        tab.nametowidget("favorite")["bg"] = STYLES[user["favorite"]][1]
        tab.nametowidget("pdp")["bg"] = STYLES[user["favorite"]][1]
        
        WINDOW.nametowidget('.!notebook').pack(fill="both",expand=1)

def user_portal():
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
        if ".editing" in [str(i) for i in WINDOW.winfo_children()]: #vérifie que l'on est pas en train d'essayer de créer un utilisateur
            win.destroy()
            pass
        elif event.widget == win: # si on essaye de ne pas se connecter sans abandonné alors le focus est remis de force (y compris lors de fenetre autre que tkinter mais j'ai pas trouvé de solution pour le moment)
            win.focus_force()

    def on_closing():
        WINDOW.nametowidget('.!notebook').pack(fill="both",expand=1)
        WINDOW.update()

        notebook = WINDOW.nametowidget('.!notebook')
        home:tk.Frame = notebook.nametowidget('home')
        notebook.select(home)
        home.focus_set()
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
    
    def create_user():
        edit_user(True,name_widget.get())
    btn = ttk.Button(center,text="Create",command=create_user)
    btn.grid(column=0,row=2,sticky="we")

    name_widget.bind("<Return>",handledata)
    name_widget.bind("<")
    win.bind("<FocusOut>", on_focus_out)
    win.protocol("WM_DELETE_WINDOW", on_closing)

def get_user():
    tab:tk.Frame = WINDOW.nametowidget('.!notebook').nametowidget('profile')
    try:
        _name:tk.Label = tab.nametowidget('pseudo')
        user = get_reader(_name['text'])
        if user: #ajouter super condition
            return user
        else:
            return False
    except KeyError:
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

def edit_user(new=False,new_name=""):
    """
    modifie un lecteur ou en ajoute 1 si le paramètre New est vrai
    """
    win = tk.Toplevel(WINDOW,name="editing")
    win.geometry("800x250")
    
    win.title("Edit profile")
    win.focus_force()

    main = ttk.Frame(win)
    main.pack(fill="both",expand=1)
    old_name = WINDOW.nametowidget('.!notebook').nametowidget('profile').nametowidget('pseudo')['text']
    if not new:
        user = get_reader(old_name)

    #region name widget
    name_widget = ttk.Label(main,name="pseudo", text="Pseudo :",padding=15)
    name_widget.grid(row=0,column=0,sticky="nw")

    #name entry
    name_entry = ttk.Entry(main)
    name_entry.grid(column=1,row=0)
    if not new:
        name_entry.insert(-1, user["name"])
    else:
        name_entry.insert(-1, new_name)

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

    if not new:
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
    
    if not new:
        rad_age[user["age"]].invoke()
    #endregion

    #region favorite widget
    favorite_widget = ttk.Label(main,name="favorite",text="Favorite style :",padding=15)
    favorite_widget.grid(row=3,column=0,sticky="nw")

    #favorite entry
    favorite_combo = ttk.Combobox(main)
    favorite_combo['values']= ("Sci-Fi", "Biography", "Horror", "Romance", "Fable", "History","Comedy","Fantasy","Thriller")
    if not new:
        favorite_combo.current(int(user["favorite"])-1)
    favorite_combo.grid(column=1, row=3)
    #endregion

    def save_data():
        new_name = name_entry.get()
        new_gender = gender_value.get()
        new_age =age_value.get()
        new_favorite = str(favorite_combo['values'].index(favorite_combo.get()) + 1)
        if new:
            try:
                add_reader(new_name,new_gender,new_age,new_favorite)
            except Exception as e:
                if 'User already exist or your name was already use' in e.args:
                    msg.showerror("USER ALREADY EXIST", "USER ALREADY EXIST !\n Please try another pseudo or if it's your account edit it.")
                    win.focus_set()
                    return
                else:
                    raise e
        else:
            update_reader(old_name=old_name,name=new_name,gender=new_gender,age=new_age,favorite=new_favorite)
        set_user(new_name)
        win.destroy()

    btn_save = ttk.Button(main,text="  Save  ",command=save_data)
    btn_save.grid(column=1,row=4,columnspan=2)

def delete_user():
    if msg.askokcancel("Delete", "Do you want to delete your account?"):
        old_name = WINDOW.nametowidget('.!notebook').nametowidget('profile').nametowidget('pseudo')['text']
        remove_reader(old_name)
        disconnect()

def generate_result(e=None,main_frame=None):
    if not main_frame:
        return
    search_bar = WINDOW.nametowidget('.!notebook').nametowidget('search').nametowidget('params').nametowidget('search_bar')
    adv_param:tk.Frame = WINDOW.nametowidget('.!notebook').nametowidget('search').getvar("adv_var")
    adv_active = WINDOW.nametowidget('.!notebook').nametowidget('search').nametowidget('foldable').show
    
    words = search_bar.get().split(" ")
    weight = len(words)//2

    main = main_frame["frame"]
    for child in main.winfo_children():
        child.destroy()
    
    result_readers = {}
    for reader in readers():
        for word in words:
            if word.upper() in reader["name"].upper().split(" ") and ((not bool(adv_active.get()) or adv_param=="user")): # from algebra : if then
                if reader["name"] in result_readers.keys():
                    result_readers[reader["name"]][0] += 1
                else:
                    result_readers[reader["name"]] = [1,"user"]
                        

    result_books = {}
    for book in books():
        for word in words:
            if word.upper() in book["name"].upper().split(" ") and ((not bool(adv_active.get()) or adv_param=="book")): # from algebra : if then
                if book["name"] in result_books.keys():
                    result_books[book["name"]][0] += 1
                else:
                    result_books[book["name"]] = [1,"book"]
                        

    all_result = {}
    all_result.update(result_books)
    all_result.update(result_readers)
    for key, value in sorted(all_result.items(),key=lambda item: -item[1][0]):
        if value[0]>= weight:
            result_widget = get_result(main,key,value[1])
            result_widget.pack(fill="x")
    
    if len(main.children)==0:
        ttk.Label(main,text="No result",name="itsme").pack(anchor='nw')
    
    main_frame["__init__"]()