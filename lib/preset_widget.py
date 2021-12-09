import tkinter as tk
from tkinter.constants import MOVETO
import tkinter.ttk as ttk

from ect.globals import GENDER, STYLES, WINDOW,AGES, Recursive_Binding
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

def get_foldable_frame(parent,window, text=""):
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
                                            variable=_frame["frame"].show)
        _frame["toggle_button"].pack(side="left",anchor="n")

        _frame["sub_frame"] = ttk.Frame(_frame["frame"],name="subframe")

        return _frame
