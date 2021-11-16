import tkinter as tk
import tkinter.ttk as ttk

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
            _dic["canvas"].xview_scroll(-event.delta, "units")
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

    _dic["canvas"] = tk.Canvas(parent,background="black",bd=0, highlightthickness=0)
    tk.Grid.rowconfigure(parent, 0, weight=1)
    tk.Grid.columnconfigure(parent, 0, weight=1)
    _dic["canvas"].grid(column=0,row=0,sticky='news')

    _dic["scrollbar"] = ttk.Scrollbar(parent,orient=tk.VERTICAL,command=_dic["canvas"].yview)
    _dic["scrollbar"].grid(column=1,row=0,sticky='ns')

    _dic["canvas"].configure(yscrollcommand=_dic["scrollbar"].set)

    _dic["frame"] = ttk.Frame(parent)
    _dic["frame_id"] = _dic["canvas"].create_window((0,0),window=_dic["frame"],anchor="nw")

    def config(e):
        _dic["canvas"].configure(scrollregion = _dic["canvas"].bbox('all'))
        _dic["canvas"].itemconfig(_dic["frame_id"], width = e.width)

    def _on_mousewheel(event):
        if not event.state:
            _dic["canvas"].yview_scroll(-event.delta, "units")
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
            _gal["canvas"].xview_scroll(-event.delta, "units")
        else:
            if parent_scroll:
                parent_scroll["_on_mousewheel"](event)
    def _bound_to_mousewheel(e):
        _gal["canvas"].bind_all("<MouseWheel>", _on_mousewheel)
    def _unbound_to_mousewheel(e):
        if parent_scroll:
            _gal["canvas"].bind_all("<MouseWheel>", parent_scroll["_on_mousewheel"])
        else:
            _gal["canvas"].unbind_all("<MouseWheel>")
    
    _gal["_on_mousewheel"] = _on_mousewheel

    _gal["canvas"].bind('<Configure>',config)
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