import tkinter as tk
from tkinter.constants import N
import tkinter.ttk as ttk

def get_horizontale_scroll_bar(parent:tk.Frame,parent_scroll:dict=None):
    _dic = {}

    _dic["canvas"] = tk.Canvas(parent,background="red")
    _dic["canvas"].pack(expand=1,fill="both")

    _dic["frame"] = tk.Frame(parent)
    _dic["frame_id"] = _dic["canvas"].create_window((0,0),window=_dic["frame"],anchor="nw")

    def config(e):
        _dic["canvas"].configure(scrollregion = _dic["canvas"].bbox('all'))
        _dic["canvas"].itemconfig(_dic["frame_id"], height = e.height)

    def _on_mousewheel(event):
        if event.state:
            _dic["canvas"].xview_scroll(-event.delta, "units")
    def _bound_to_mousewheel(e):
        _dic["canvas"].bind_all("<MouseWheel>", _on_mousewheel)
    def _unbound_to_mousewheel(e):
        parent_func = None
        if parent_scroll:
            parent_func = parent_scroll["_on_mousewheel"]
        _dic["canvas"].bind_all("<MouseWheel>", parent_func or None)
    
    _dic["_on_mousewheel"] = _on_mousewheel

    _dic["canvas"].bind('<Configure>',config)
    _dic["frame"].bind('<Enter>', _bound_to_mousewheel)
    _dic["frame"].bind('<Leave>', _unbound_to_mousewheel)

    return _dic




