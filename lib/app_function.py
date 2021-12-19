import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from PIL import Image
from PIL.ImageTk import PhotoImage

from ect.globals import AGES, WINDOW,STYLES,GENDER,Recursive_Binding,force_update
from tkinter.constants import MOVETO
from lib.users_functions import *
from lib.books_functions import *

"""
this file contain all the pre-build complex widget used in the project or all the fonction that link all data functions and the app itself
"""
def get_gallery(parent:tk.Frame,parent_scroll:dict=None):
    """
    this function return a dictionary with a pre-build gallery widget for the home page
    
    the dictionary contain :
        - the main frame scrollable
        - the scroll function if we want to bind it from a child
        - the refesh function for windows
        - the list of pannels in the gallery
        - the function to add a panel to the gallery
    """
    _gal = {}

    _gal["canvas"] = tk.Canvas(parent,bd=0, highlightthickness=0) #only canva can be scroll in tkinter
    _gal["canvas"].pack(expand=1,fill="both")

    _gal["frame"] = ttk.Frame(parent)
    
    def refresh():
        """
        function update the page and the region of scroll at each update
        """
        WINDOW.update()
        _gal["canvas"].configure(scrollregion = _gal["canvas"].bbox('all'))
    _gal["refresh"] = lambda:refresh()
    
    _gal["frame_id"] = _gal["canvas"].create_window((0,0),window=_gal["frame"],anchor="nw")

    def config(e):
        """
        this function update the window each time the main window is updated, we need to recalcul the coef for the scroll and update the region of scroll and the height of the window which bug a little else
        """
        _gal["coef_scroll"] = _gal["frame"].winfo_width()/parent.winfo_width()*40
        _gal["canvas"].configure(scrollregion = _gal["canvas"].bbox('all'))
        _gal["canvas"].itemconfig(_gal["frame_id"], height = e.height)
    def _on_mousewheel(event):
        """
        this function update the view on scroll, if there is a parent scroll we update it in case we aren't updating our
        """
        if event.state%2: #this check if we are scrolling on vertical or horizontal axis
            offset = -event.delta/(_gal["coef_scroll"] * abs(event.delta))
            _gal["scroll_pos"] += offset if (_gal["scroll_pos"]+offset > 0 and _gal["scroll_pos"]+offset < 1) else 0
            _gal["canvas"].xview(MOVETO,_gal["scroll_pos"])
        else:
            if parent_scroll:
                parent_scroll["_on_mousewheel"](event)
                WINDOW.update()
    def _bound_to_mousewheel(e):
        """
        this function add the scroll function to the event when we are in the frame/gallery
        """
        _gal["canvas"].bind_all("<MouseWheel>", _on_mousewheel)
    def _unbound_to_mousewheel(e):
        """
        this function unadd the scroll function to the event when we are in the frame/gallery and if a parent have a function of scroll we add its
        """
        if parent_scroll:
            _gal["canvas"].bind_all("<MouseWheel>", parent_scroll["_on_mousewheel"])
        else:
            _gal["canvas"].unbind_all("<MouseWheel>")
    
    _gal["_on_mousewheel"] = _on_mousewheel

    _gal["canvas"].bind('<Configure>',config)
    _gal["scroll_pos"] = 0
    _gal["canvas"].yview(MOVETO,_gal["scroll_pos"])
    _gal["frame"].bind('<Enter>', _bound_to_mousewheel)
    _gal["frame"].bind('<Leave>', _unbound_to_mousewheel)

    _gal["panels"] = {}

    def __add_panel__(object,self,direction:str="left"):
        """
        this function add a panel to the gallery and stock it to be easily access again
        """
        self["panels"][object["name"]] = object["frame"]
        
        _pad = ttk.Frame(self["frame"],width=25)
        _pad.pack(side=direction)
        
        self["panels"][object["name"]].grid_propagate(0)
        self["panels"][object["name"]].pack(side=direction,expand=1,fill="x")
        object["text"].place(relx=0.5, rely=0.5, anchor="center")
        
        func = lambda e:display_book(object["name"])
        Recursive_Binding(object["frame"],"<Double-Button-1>",func)
        
        _pad = ttk.Frame(self["frame"],width=25)
        _pad.pack(side=direction)

    _gal["__add_panel__"] = __add_panel__
    
    return _gal

def get_vertical_scroll_bar(parent:ttk.Frame,parent_scroll:dict=None):
    """
    this function return a dictionary with a pre-build scrollable frame widget for the home page and the search tab
    
    the dictionary contain :
        - the main frame scrollable
        - the scroll function if we want to bind it from a child
        - the refesh function for Windows

    all the listed function work the same as the gallery's ones
    """
    _dic = {}

    _dic["canvas"] = tk.Canvas(parent,bd=0, highlightthickness=0)
    tk.Grid.rowconfigure(parent, 0, weight=1)
    tk.Grid.columnconfigure(parent, 0, weight=1)
    _dic["canvas"].grid(column=0,row=0,sticky='news')

    _dic["scrollbar"] = ttk.Scrollbar(parent,orient=tk.VERTICAL,command=_dic["canvas"].yview)
    _dic["scrollbar"].grid(column=1,row=0,sticky='ns')

    _dic["canvas"].configure(yscrollcommand=_dic["scrollbar"].set)

    _dic["frame"] = ttk.Frame(parent,name="vertical_scroll_frame")
    _dic["frame_id"] = _dic["canvas"].create_window((0,0),window=_dic["frame"],anchor="nw")

    # even if the canvas is empty we have a not white and empty background
    ttk.Frame(_dic["canvas"]).pack(fill="both",expand=1,side="bottom")

    def config(e):
        _dic["coef_scroll"] = _dic["frame"].winfo_height()**(1/3)/parent.winfo_height()**(1/3)*20
        _dic["canvas"].configure(scrollregion = _dic["canvas"].bbox('all'))
        _dic["canvas"].itemconfig(_dic["frame_id"], width = e.width)
    def _on_mousewheel(event):
        if not event.state%2:
            offset = -event.delta/(_dic["coef_scroll"] * abs(event.delta))
            _dic["scroll_pos"] = _dic["scrollbar"].get()[0] #value can be modify so we get it again
            _dic["scroll_pos"] += offset
            _dic["canvas"].yview(MOVETO,_dic["scroll_pos"])
    def _bound_to_mousewheel(e):
        _dic["canvas"].bind_all("<MouseWheel>", _on_mousewheel)
    def _unbound_to_mousewheel(e):
        if parent_scroll:
            _dic["canvas"].bind_all("<MouseWheel>", parent_scroll["_on_mousewheel"])
        else:
            _dic["canvas"].unbind_all("<MouseWheel>")

    # store the function to be able to get it back later in case we go from teh child to the parent (rebind the appropriate function)
    _dic["_on_mousewheel"] = _on_mousewheel

    _dic["scroll_pos"] = _dic["scrollbar"].get()[1] - _dic["scrollbar"].get()[0]
    _dic["canvas"].yview(MOVETO,_dic["scroll_pos"])
    _dic["canvas"].configure(scrollregion = _dic["canvas"].bbox('all'))
    _dic["canvas"].bind('<Configure>',config)
    _dic["frame"].bind('<Enter>', _bound_to_mousewheel)
    _dic["frame"].bind('<Leave>', _unbound_to_mousewheel)

    
    def refresh():
        WINDOW.update() # doit etre au début pour que les valeur soit bien update avant les recalculs
        _dic["coef_scroll"] = _dic["frame"].winfo_height()**(1/3)/parent.winfo_height()**(1/3)*20
        _dic["canvas"].configure(scrollregion = _dic["canvas"].bbox('all'))
        _dic["canvas"].itemconfig(_dic["frame_id"], width = _dic["canvas"].winfo_width())
    _dic["refresh"] = lambda:refresh()

    return _dic

def get_foldable_frame(parent,window, text=""):
    """
    this function return a foldable frame in a dictionary
    """
    _frame = {"frame":ttk.Frame(parent ,name="foldable",padding=10)}

    _frame["frame"].show = tk.IntVar()
    _frame["frame"].show.set(0)

    _frame["title_frame"] = ttk.Frame(_frame["frame"])
    _frame["title_frame"].pack(anchor="nw")

    ttk.Label(_frame["title_frame"], text=text).pack(side="left", fill="x", expand=1,anchor="n")

    def toggle():
        if bool(_frame["frame"].show.get()):
            _frame["sub_frame"].pack(fill="x", expand=1)
            window.update()
        else:
            _frame["sub_frame"].forget()


    _frame["toggle_button"] = ttk.Checkbutton(_frame["title_frame"], width=2, command=toggle,
                                        variable=_frame["frame"].show)# we bind the command of the button to the update of the frame
    _frame["toggle_button"].pack(side="left",anchor="n")

    _frame["sub_frame"] = ttk.Frame(_frame["frame"],name="subframe") #this is the foldable frame

    return _frame

def display_user(name):
    """
    this function create a pop-up window wich show us the info of a user
    """
    win = tk.Toplevel(WINDOW)
    win.geometry("343x122")
    
    win.title(name)
    win.focus_force()

    main = ttk.Frame(win)
    main.pack(fill="both",expand=1)

    user = get_reader(name)

    span = ttk.Label(main,padding=50)
    span.grid(column=0,row=0,rowspan=1000)
    name_widget = ttk.Label(main,name="pseudo", text=name)
    name_widget.grid(column=1,row=0)
    gender_widget = ttk.Label(main,name="gender", text=GENDER[user["gender"]])
    gender_widget.grid(column=1,row=1)
    age_widget = ttk.Label(main,name="age",text=AGES[user["age"]])
    age_widget.grid(column=1,row=2)
    pdp_favorite = tk.Frame(main,name="pdp",width=100,height=50,bg=STYLES[user["favorite"]][1])
    pdp_favorite.grid(column=1,row=3)
    favorite_widget = tk.Label(main,name="favorite",text=STYLES[user["favorite"]][0],background=STYLES[user["favorite"]][1])
    favorite_widget.grid(column=1,row=3)

    func = lambda e:win.destroy()
    win.bind("<FocusOut>",func) # to avoid multiple windows we close it on the loss of focus

def display_book(name):
    """
    this function is a pop up window which show the info on the book and allow different action if the user is connected
    """
    win = tk.Toplevel(WINDOW,name="display_book")
    win.geometry("303x137")
    win.title(name)
    
    win.focus_force()

    main = ttk.Frame(win,name="main")
    main.pack(fill="both",expand=1)

    book = get_book(name)
    try:
        user = get_reader(WINDOW.nametowidget('.!notebook').nametowidget('profile').nametowidget('pseudo')['text'])
    except:
        user = False

    # name of the book
    name_widget = ttk.Label(main,name="pseudo", text=name,wraplength=150,justify="center")
    name_widget.grid(column=0,row=0,padx=10)
    # bouton read/unread
    if not user:
        status_widget = ttk.Label(main,name="status",text="not connected")
        status_widget.grid(column=0,row=2)
    else:
        readings = get_readings(user["name"])
        def unread_func():
                unread_book(user["name"],name)
                note_book(book,user,0)
                on_click_double()
                status_bouton.configure(text="read")
                status_bouton.configure(command=read_func)
        def read_func():
                read_book(user["name"],name)
                status_bouton.configure(text="unread")
                status_bouton.configure(command=unread_func)
        
        if name in readings.values():
            status_bouton = ttk.Button(main,text="unread",command=unread_func)
            status_bouton.grid(column=0,row=2)
        else:
            status_bouton = ttk.Button(main,text="read",command=read_func)
            status_bouton.grid(column=0,row=2)
    # global rating of the book
    global_rating_widget = ttk.Label(main,name="global_rating",text=get_global_rating(name) or "not enougth notes")
    global_rating_widget.grid(column=0,row=1)
    # frame color of the book
    pdp_favorite = tk.Frame(main,name="pdp",width=100,height=50,bg=STYLES[book["style"]][1])
    pdp_favorite.grid(column=1,row=0,rowspan=4,sticky="ns")
    # style of the book
    style_widget = tk.Label(main,name="style",text=STYLES[book["style"]][0],bg=STYLES[book["style"]][1],fg=STYLES[book["style"]][2])
    style_widget.grid(column=1,row=0,rowspan=4)
    #buttons
    
    #delete
    def func():
        if msg.askokcancel("Delete", "Do you want to delete the book ?"):
            remove_book(name)
            win.destroy()
    #edit
    def edit_func():
        edit_book(False)
        
    btn_edit = ttk.Button(main,text="edit",command=edit_func)
    btn_edit.grid(column=0,row=4)
    btn_delt = ttk.Button(main,text="delete",command=func)
    btn_delt.grid(column=1,row=4)

    # this is the frame witch contain the star that allow us to note a book
    frame = ttk.Frame(main)
    frame.grid(column=0,row=3) 
    
    star_grey = Image.open(PATH / "sprite" / "star_grey.gif").convert("RGBA").resize((15,15))
    star_grey_tk = PhotoImage(image=star_grey)

    star = Image.open(PATH / "sprite" / "star.gif").convert("RGBA").resize((15,15))
    star_tk = PhotoImage(image=star)
    
    stars = [ttk.Label(frame,image=star_grey_tk,name=f"{i+1}") for i in range(5)]
    
    def on_click(e=None):
        """
        this function update the note if connected and update the GUI
        """
        if user: # we check if the user is connected (was when we opened the window but since it close on the loss of focus this don't create bug)
            if str(book["index"]) in get_readings(user["name"]): # we check if the user read it
                img = star_tk
                alt_img = star_grey_tk
                number = int(str(e.widget)[-1])

                for lab in stars[:number]: #this pass all star before our note (included) in yellow
                    lab.configure(image=img)
                    lab.photo = img
                else: # and all the other in grey
                    for lab in stars[number:]:
                        lab.configure(image=alt_img)
                        lab.photo = img
                note_book(book,user,number)
            else:
                on_click_double()
                msg.askokcancel("YOU MUST READ THE BOOK TO RATE IT", "YOU MUST READ THE BOOK TO RATE IT \n Please read the book before trying to read it.") 
        else:
            msg.askokcancel("USER NOT CONNECTED", "YOU ARE NOT CONNECTED \n Please connect yourself in the account pannel before using this function.")
    def on_click_double(e=None):
        """
        this function remove all star and unnote a book
        """
        img = star_grey_tk
        
        for lab in stars:
            lab.configure(image=img)
            lab.photo = img
        
        if user:
            note_book(book,user,0)
    
    for i,star in enumerate(stars):
        Recursive_Binding(star,"<Button-1>",on_click) #this is a function we create to bind all child of a widget so if we click on them (like on the text and not the button directly) the action will be effectued
        Recursive_Binding(star,"<Double-Button-1>",on_click_double)
        if user and str(book["index"]) in get_readings(user["name"]): #this configure the star at the start
            if int(get_note(user,book))>i:
                star.configure(image=star_tk)
                star.photo = star_tk
        else:
            star.photo = star_grey_tk

        star.pack(fill="both", expand=1,side='left',padx=2)

    func = lambda e:win.destroy() #this destroy the window if we lose focus
    win.bind("<FocusOut>",func)

def user_portal():
    """
    this is a pop up window which allow the user to connect himself in the app
    """
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
        if ".editing" in [str(i) for i in WINDOW.winfo_children()]: # check if we are not trying to create a new user
            win.destroy()
            pass
        elif event.widget == win: # if we want to on the app without connect or cancel, the focus is set again
            win.focus_force()

    def on_closing():
        """
        this function permit the user to abandon the connection by closing the window
        """
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
        """
        this function connect the user to the app
        """
        name = name_widget.get()
        if name:
            set_user(name)
            win.destroy()

    btn = ttk.Button(center,text="Connect",command=handledata)
    btn.grid(column=0,row=1,sticky="we")
    
    def create_user():
        """
        this function call the function to create a new user, since we lose focus this window is closed automatically
        """
        name = name_widget.get() if not get_reader(name_widget.get()) else ""
        edit_user(True,name)
    btn = ttk.Button(center,text="Create",command=create_user)
    btn.grid(column=0,row=2,sticky="we")

    name_widget.bind("<Return>",handledata)
    win.bind("<FocusOut>", on_focus_out)
    win.protocol("WM_DELETE_WINDOW", on_closing)

def edit_user(new=False,new_name=""):
    """
    this is a pop up window to create or update a user
    """
    win = tk.Toplevel(WINDOW,name="editing")
    win.geometry("800x250")
    
    win.title("profile edition")
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
    rad_age["1"] = ttk.Radiobutton(main,text='<18 years old',variable=age_value, value="1",command=age_value.get);rad_age["1"].grid(column=1, row=2)
    rad_age["2"] = ttk.Radiobutton(main,text='Between 18 and 25 years old',variable=age_value, value="2",command=age_value.get);rad_age["2"].grid(column=2,row=2)
    rad_age["3"] = ttk.Radiobutton(main,text='>25 years old',variable=age_value, value="3",command=age_value.get);rad_age["3"].grid(column=3,row=2)
    
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
        """
        this function try to save the data or raise warning if we can't
        """
        if name_entry.get().isdigit():
            name_entry.delete(0,"end")
            msg.showerror("USER NAME CANNOT BE A NUMBER", "USER NAME CANNOT BE A NUMBER !\n Please try another pseudo.")
            return
        new_name = name_entry.get()
        new_gender = gender_value.get()
        new_age =age_value.get()
        new_favorite = str(favorite_combo['values'].index(favorite_combo.get()) + 1)
        try:
            if new:
                    new_name = new_name.replace(",","")
                    if not new_name:
                        msg.showerror("INVALID NAME", "INVALID NAME !\n Please try another pseudo.")
                        return
                    add_reader(new_name,new_gender,new_age,new_favorite)
            else:
                update_reader(old_name=old_name,name=new_name,gender=new_gender,age=new_age,favorite=new_favorite)
            set_user(new_name)
            win.destroy()
        except UserWarning:
                msg.showerror("USER ALREADY EXIST", "USER ALREADY EXIST !\n Please try another pseudo or if it's your account edit it.")
                win.focus_set()
                return

    btn_save = ttk.Button(main,text="  Save  ",command=save_data)
    btn_save.grid(column=1,row=4,columnspan=2)

def edit_book(new=True):
    """
    this function create a pop up window to allow us to update or create a book
    """
    if not new:
        old_name = WINDOW.nametowidget('display_book').nametowidget('main').nametowidget('pseudo')["text"]
        try:
            book = get_book(old_name)
        except:
            new=False
    win = tk.Toplevel(WINDOW,name="book_adding")
    win.geometry("800x250")
    
    win.title("book edition")
    win.focus_force()

    # overide of the main app
    WINDOW.nametowidget('.!notebook').pack_forget()
    WINDOW.nametowidget('.!notebook').update()
    force_update()

    main = ttk.Frame(win)
    main.pack(fill="both",expand=1)

    #region name widget
    name_widget = ttk.Label(main,name="pseudo", text="Title :",padding=15)
    name_widget.grid(row=0,column=0,sticky="nw")
    
    #name entry
    name_entry = ttk.Entry(main)
    name_entry.grid(column=1,row=0)
    if not new:
        name_entry.insert(-1, book["name"])

    #endregion

    #region favorite widget
    favorite_widget = ttk.Label(main,name="favorite",text="Style :",padding=15)
    favorite_widget.grid(row=3,column=0,sticky="nw")

    #favorite entry
    favorite_combo = ttk.Combobox(main)
    favorite_combo['values']= ("Sci-Fi", "Biography", "Horror", "Romance", "Fable", "History","Comedy","Fantasy","Thriller")
    if not new:
        favorite_combo.current(int(book["style"])-1)
    
    favorite_combo.grid(column=1, row=3)
    #endregion

    def return_home():
        """
        this function allow us to abandon the creation of a book by closing the window
        """
        WINDOW.nametowidget('.!notebook').pack(fill="both",expand=1)
        WINDOW.update()

        if new:
            onglets = WINDOW.nametowidget('.!notebook')
            home = WINDOW.nametowidget('.!notebook').nametowidget('home')
            onglets.select(home); home.focus_set()
        win.destroy()

    def save_data():
        """
        this function try to save the data or raise warning if we can't
        """
        new_name = name_entry.get()
        new_favorite = str(favorite_combo['values'].index(favorite_combo.get()) + 1)
        try:
            if new:
                add_book(new_name,new_favorite)
                return_home()
            else:
                update_book(old_name,name=new_name,style=new_favorite)
                return_home()
        except UserWarning as e:
            msg.showerror("BOOK ALREADY EXIST", "BOOK ALREADY EXIST !\n Please try another title.")
            win.focus_set()
            return

    btn_save = ttk.Button(main,text="  Save  ",command=save_data)
    btn_save.grid(column=1,row=4,columnspan=2)
    
    win.protocol("WM_DELETE_WINDOW", return_home)

def generate_result(e=None,main_frame=None):
    """
    this automatically add result of the search bar to the main_frame in argument
    the fonction work by weigth, the more it look like what we want the more higher it will be in the result's frame
    """
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
            if word.upper() in reader["name"].upper() and ((not bool(adv_active.get()) or adv_param=="user")): # from algebra : if then
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
    
    main_frame["refresh"]()

def get_result(parent,name,type):
    """
    this return a frame which represent a result, we can double click it for more information
    """
    if type=="book":
        _res = {}
        book = get_book(name)

        _res["frame"] = ttk.Frame(parent,relief='raised',padding=10)
        _res["title"] = ttk.Label(_res["frame"],text=name,font=("Arial Bold", 18))
        _res["title"].grid(column=0,row=0,sticky="w")
        _res["second_line"]= ttk.Frame(_res["frame"])
        _res["second_line"].grid(column=0,row=1,sticky="w")
        _res["type"] = ttk.Label(_res["second_line"],text=type,font=("Arial Italic",))
        _res["type"].grid(column=0,row=0,sticky="w")
        user = WINDOW.nametowidget('.!notebook').nametowidget('profile').nametowidget('pseudo')['text']
        if user=="":
            _res["status"] = ttk.Label(_res["second_line"],text="not connected",font=("Arial Italic",))
        else:
            readings = get_readings(WINDOW.nametowidget('.!notebook').nametowidget('profile').nametowidget('pseudo')['text'])
            if name in readings.values():
                _res["status"] = ttk.Label(_res["second_line"],text="read",font=("Arial Italic",))
            else:
                _res["status"] = ttk.Label(_res["second_line"],text="not read",font=("Arial Italic",))
        _res["status"].grid(column=1,row=0,sticky="w")

        func = lambda e:display_book(name)
        Recursive_Binding(_res["frame"],"<Double-Button-1>",func)
    elif type=="user":
        _res = {}
        user = get_reader(name)

        _res["frame"] = ttk.Frame(parent,relief='raised',padding=10)
        _res["title"] = ttk.Label(_res["frame"],text=name,font=("Arial Bold", 18))
        _res["title"].grid(column=0,row=0,sticky="w")
        _res["second_line"]= ttk.Frame(_res["frame"])
        _res["second_line"].grid(column=0,row=1,sticky="w")
        gender = GENDER[user["gender"]]
        _res["gender"] = ttk.Label(_res["second_line"],text=gender,font=("Arial Italic",))
        _res["gender"].grid(column=0,row=0,sticky="w")
        style = STYLES[user["favorite"]][0]
        _res["style"] = ttk.Label(_res["second_line"],text=style,font=("Arial Italic",))
        _res["style"].grid(column=1,row=0,sticky="w")
        
        func = lambda e:display_user(name)
        Recursive_Binding(_res["frame"],"<Double-Button-1>",func)
    
    return _res["frame"]

def set_user(name):
    """
    this function set the GUI with the value of the user we are connecting with
    """
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

def get_user():
    """
    this return the user with which we are connected by getting the name in the GUI, if no user or error we return false
    """
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
    """
    this disconnect the user from the app by removing the information in the GUI
    """
    tab:tk.Frame = WINDOW.nametowidget('.!notebook').nametowidget('profile')

    tab.nametowidget("pseudo")["text"] = ""
    tab.nametowidget("gender")["text"] = ""
    tab.nametowidget("age")["text"] = ""
    tab.nametowidget("favorite")["text"] = ""
    tab.nametowidget("pdp")["bg"] = "white"

    onglets = WINDOW.nametowidget('.!notebook')
    home = WINDOW.nametowidget('.!notebook').nametowidget('home')
    onglets.select(home); home.focus_set()

def delete_user():
    """
    this function delete the user with which we are connected
    """
    if msg.askokcancel("Delete", "Do you want to delete your account?"):
        old_name = WINDOW.nametowidget('.!notebook').nametowidget('profile').nametowidget('pseudo')['text']
        remove_reader(old_name)
        disconnect()
