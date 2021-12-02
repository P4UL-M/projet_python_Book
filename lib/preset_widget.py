import tkinter as tk
from tkinter.constants import MOVETO
import tkinter.ttk as ttk

from ect.globals import GENDER, STYLES, WINDOW,AGES
from lib.books_functions import *
from lib.users_functions import *

def get_horizontale_scroll_bar(parent:ttk.Frame,parent_scroll:dict=None):
    _dic = {}

    _dic["canvas"] = tk.Canvas(parent,bd=0, highlightthickness=0)
    _dic["canvas"].pack(expand=1,fill="both")

    _dic["frame"] = ttk.Frame(parent)
    _dic["frame_id"] = _dic["canvas"].create_window((0,0),window=_dic["frame"],anchor="nw")

    def config(e):
        _dic["canvas"].configure(scrollregion = _dic["canvas"].bbox('all'))
        _dic["canvas"].itemconfig(_dic["frame_id"], height = e.height)

    def _on_mousewheel(event):
        if event.state:
            _dic["canvas"].xview_scroll(event.delta, "units")
        else:
            if parent_scroll:
                parent_scroll["_on_mousewheel"](event)
    def _bound_to_mousewheel(e):
        _dic["canvas"].bind_all("<MouseWheel>", _on_mousewheel)
    def _unbound_to_mousewheel(e):
        if parent_scroll:
            _dic["canvas"].bind_all("<MouseWheel>", parent_scroll["_on_mousewheel"])
        else:
            _dic["canvas"].unbind_all("<MouseWheel>")
    
    _dic["_on_mousewheel"] = _on_mousewheel

    _dic["canvas"].bind('<Configure>',config)
    _dic["frame"].bind('<Enter>', _bound_to_mousewheel)
    _dic["frame"].bind('<Leave>', _unbound_to_mousewheel)

    return _dic

def get_vertical_scroll_bar(parent:ttk.Frame,parent_scroll:dict=None):
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
    ttk.Frame(_dic["canvas"]).pack(fill="both",expand=1)

    def config(e):
        if "offset" in _dic.keys():
            _dic.pop("offset")
        _dic["canvas"].configure(scrollregion = _dic["canvas"].bbox('all'))
        _dic["canvas"].itemconfig(_dic["frame_id"], width = e.width)
    def _on_mousewheel(event):
        if "offset" not in _dic.keys():
            # to get the perfect value of the actual position i update it with the position of the scroll bar but it has a small offset between th two value
            _dic["offset"] = _dic["scrollbar"].get()[1]
        if not event.state:
            offset = -event.delta/120
            _dic["scroll_pos"] = _dic["scrollbar"].get()[1] - _dic["offset"]
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

    _dic["scroll_pos"] = 0
    _dic["canvas"].yview(MOVETO,_dic["scroll_pos"])
    _dic["canvas"].configure(scrollregion = _dic["canvas"].bbox('all'))
    _dic["canvas"].bind('<Configure>',config)
    _dic["frame"].bind('<Enter>', _bound_to_mousewheel)
    _dic["frame"].bind('<Leave>', _unbound_to_mousewheel)

    def __init__():
        if "offset" in _dic.keys(): # we suppress the offset so it not stay with the old one
            _dic.pop("offset")
        _dic["canvas"].configure(scrollregion = _dic["canvas"].bbox('all')) #update the region of scroll
        _dic["scroll_pos"] = 0 # since we update the offset we need to update all other things
        _dic["canvas"].yview(MOVETO,_dic["scroll_pos"])
        
    # store a init function for when we update the results    
    _dic["__init__"] = __init__

    return _dic

def get_gallery(parent:tk.Frame,parent_scroll:dict=None):
    _gal = {}

    _gal["canvas"] = tk.Canvas(parent,bd=0, highlightthickness=0)
    _gal["canvas"].pack(expand=1,fill="both")

    _gal["frame"] = ttk.Frame(parent)
    _gal["frame_id"] = _gal["canvas"].create_window((0,0),window=_gal["frame"],anchor="nw")

    def config(e):
        _gal["canvas"].configure(scrollregion = _gal["canvas"].bbox('all'))
        _gal["canvas"].itemconfig(_gal["frame_id"], height = e.height)
    def _on_mousewheel(event):
        if event.state:
            offset = -event.delta/120
            _gal["scroll_pos"] += offset if (_gal["scroll_pos"]+offset > 0 and _gal["scroll_pos"]+offset < 1) else 0
            _gal["canvas"].xview(MOVETO,_gal["scroll_pos"])
        else:
            if parent_scroll:
                parent_scroll["_on_mousewheel"](event)
                WINDOW.update()
    def _bound_to_mousewheel(e):
        _gal["canvas"].bind_all("<MouseWheel>", _on_mousewheel)
    def _unbound_to_mousewheel(e):
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
        self["panels"][object["name"]] = object["frame"]
        _pad = ttk.Frame(self["frame"],width=25)
        _pad.pack(side=direction)
        self["panels"][object["name"]].pack(side=direction,expand=1,fill="x")
        _pad = ttk.Frame(self["frame"],width=25)
        _pad.pack(side=direction)

    _gal["__add_panel__"] = __add_panel__
    
    return _gal

def get_foldable_frame(parent,window, text=""):
        _frame = {"frame":ttk.Frame(parent,padding=10)}

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
                                            variable=_frame["frame"].show)
        _frame["toggle_button"].pack(side="left",anchor="n")

        _frame["sub_frame"] = ttk.Frame(_frame["frame"])

        return _frame

def get_result_book(parent,name,type):
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
        _res["frame"].bind("<Double-Button-1>", func)
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
        _res["frame"].bind("<Double-Button-1>", func)
    
    return _res["frame"]

def display_user(name):
    win = tk.Toplevel(WINDOW)
    win.geometry("343x122")
    
    win.title(name)
    win.focus_force()

    main = ttk.Frame(win)
    main.pack(fill="both",expand=1)

    user = get_reader(name)

    name_widget = ttk.Label(main,name="pseudo", text=name)
    name_widget.pack()
    gender_widget = ttk.Label(main,name="gender", text=GENDER[user["gender"]])
    gender_widget.pack()
    age_widget = ttk.Label(main,name="age",text=AGES[user["age"]])
    age_widget.pack()
    favorite_widget = ttk.Label(main,name="favorite",text=STYLES[user["favorite"]][0])
    favorite_widget.pack()
    pdp_favorite = tk.Frame(main,name="pdp",width=50,height=50,bg=STYLES[user["favorite"]][1])
    pdp_favorite.pack()

    func = lambda e:win.destroy()
    win.bind("<FocusOut>",func)

def display_book(name):
    win = tk.Toplevel(WINDOW)
    win.geometry("343x122")
    
    win.title(name)
    win.focus_force()

    main = ttk.Frame(win)
    main.pack(fill="both",expand=1)

    book = get_book(name)

    name_widget = ttk.Label(main,name="pseudo", text=name)
    name_widget.pack()
    status_widget = ttk.Label(main,name="status",text="")
    status_widget.pack()
    favorite_widget = ttk.Label(main,name="favorite",text=STYLES[book["style"]][0])
    favorite_widget.pack()
    pdp_favorite = tk.Frame(main,name="pdp",width=50,height=50,bg=STYLES[book["style"]][1])
    pdp_favorite.pack()

    func = lambda e:win.destroy()
    win.bind("<FocusOut>",func)