import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import tkinter.filedialog as tkfile
import sys

from lib.books_functions import books
from lib.users_functions import get_readings
from lib.app_function import *
from ect.globals import WINDOW

tab_control = ttk.Notebook(WINDOW)
#region onglet menu
# create the 3 tabs and add it to the tab_control
Part1 = ttk.Frame(tab_control,name="home"); tab_control.add(Part1, text='For you')
Part2 = ttk.Frame(tab_control,name="search"); tab_control.add(Part2, text='Search')
Part3 = ttk.Frame(tab_control,name='profile'); tab_control.add(Part3, text='My Account')
Part4 = ttk.Frame(tab_control,name='add_a_book'); tab_control.add(Part4, text='Add a Book')

# organisation of the tabs
tab_control.pack(expand=1, fill='both')
#endregion

#region PART 1
#region confingscroll bar main
wrapper1 = ttk.Frame(Part1,padding=15)

_frame_scrollable_main = get_vertical_scroll_bar(wrapper1)
_frame_main = _frame_scrollable_main["frame"]

wrapper1.pack(fill='both',expand=1)
#endregion

#region RECOMMENDATION
container_recommandation = ttk.Frame(_frame_main)
container_recommandation.pack(expand=1,fill="x")
lbl = ttk.Label(container_recommandation, text="RECOMMANDATION :",font=("Arial Bold", 25),padding=15)
lbl.pack(side="top", anchor="w")

#region configscroll bar recommandation
wrapper_rec = ttk.Frame(container_recommandation)

recommendation_gallery = get_gallery(wrapper_rec,_frame_scrollable_main)

wrapper_rec.pack(side=tk.TOP,fill='x',expand=1)
#endregion

for i in range(10):
    book = {
        "name":f"book{str(i)}",
        "frame":tk.Frame(recommendation_gallery["frame"],height=180,width=100,background="black")
        }
    #recommendation_gallery["__add_panel__"](book,recommendation_gallery)
#endregion

#region News
container_new = ttk.Frame(_frame_main)
container_new.pack(expand=1,fill="x")
lbl = ttk.Label(container_new, text="RECENTLY ADDED :",font=("Arial Bold", 25),padding=15)
lbl.pack(side="top", anchor="w")

#region configscroll bar News
wrapper_new = ttk.Frame(container_new)

new_gallery = get_gallery(wrapper_new,_frame_scrollable_main)

wrapper_new.pack(side=tk.TOP,fill='x',expand=1)
#endregion
def update_gallery_News():    
    if "offset" in new_gallery.keys():
        new_gallery["offset"].forget()
    
    for child in new_gallery["frame"].winfo_children():
        child.forget()

    enum = zip(range(10),[i for i in books()][::-1])

    for i,book in enum:
        frame = tk.Frame(new_gallery["frame"],height=180,width=100,background=STYLES[book["style"]][1])
        text = tk.Label(frame,text=book["name"],fg=STYLES[book["style"]][2],bg=STYLES[book["style"]][1],wraplength=100)
        book = {
            "name":book["name"],
            "frame":frame,
            "text":text
        }
        new_gallery["__add_panel__"](book,new_gallery)
    
    new_gallery["offset"] = ttk.Frame(new_gallery["canvas"],height=180,border=1)
    new_gallery["offset"].pack(expand=1,fill="both",side="right")
    
update_gallery_News()
#endregion

#region RATE
container_rate = ttk.Frame(_frame_main)
container_rate.pack(expand=1,fill="x")
lbl = ttk.Label(container_rate, text="YOU MAYBE WANT TO RATE :",font=("Arial Bold", 25),padding=15)
lbl.pack(side="top", anchor="w")

#region configscroll bar Rate
wrapper_rate = tk.Frame(container_rate,background="blue")

rate_gallery = get_gallery(wrapper_rate,_frame_scrollable_main)

wrapper_rate.pack(side=tk.TOP,fill='x',expand=1)
#endregion
def update_gallery_Rate():
    user = get_user() 
    
    if "offset" in rate_gallery.keys():
        rate_gallery["offset"].forget()
    
    if user:
        for child in rate_gallery["frame"].winfo_children():
            child.forget()

        enum = [i for i in get_readings(user["name"])][::-1]
        
        for index in enum:
            for book in books():
                if str(book["index"])==index:
                    enum[enum.index(index)] = book
                    break

        for book in enum:
            frame = tk.Frame(rate_gallery["frame"],height=180,width=100,background=STYLES[book["style"]][1])
            text = tk.Label(frame,text=book["name"],fg=STYLES[book["style"]][2],bg=STYLES[book["style"]][1],wraplength=100)
            book = {
                "name":book["name"],
                "frame":frame,
                "text":text
                }
            rate_gallery["__add_panel__"](book,rate_gallery)
    
    rate_gallery["offset"] = ttk.Frame(rate_gallery["canvas"],height=180,border=1)
    rate_gallery["offset"].pack(expand=1,fill="both",side="right")
    

update_gallery_Rate()
#endregion

#region actualise on focus
def actualise(event):
    if event.widget == Part1:
        WINDOW.update()
        update_gallery_Rate()
        update_gallery_News()

Part1.bind("<FocusIn>", actualise)
#endregion

#endregion

#region PART 2
frame_search_bar = ttk.Frame(Part2,padding=15,name="params")

frame_search_bar.pack(fill="x")

# init zone result before param because we need it but it's pack after
wrapper_zone = tk.Frame(Part2,background="red",name="wrapper")
zone = get_vertical_scroll_bar(wrapper_zone)

func = lambda e=None:generate_result(main_frame=zone)

#region Search Bar elts
txt = ttk.Entry(frame_search_bar,name="search_bar")
txt.pack(side="left",fill="x",expand=1)
txt.focus()
txt.bind("<Return>",func)

btn = ttk.Button(frame_search_bar,text="Enter",command=func)
btn.pack(side="right")
#endregion

adv_param = get_foldable_frame(Part2,WINDOW,text="Advanced settings")
adv_param["frame"].pack(anchor="w")

#region Adv param elt

rad_adv = dict()
adv_value = tk.StringVar(Part2,name="adv_var")
rad_adv["1"] = ttk.Radiobutton(adv_param["sub_frame"],text='Book',variable=adv_value, value="book",command=adv_value.get);rad_adv["1"].grid(column=0, row=0)
rad_adv["2"] = ttk.Radiobutton(adv_param["sub_frame"],text='User',variable=adv_value, value="user",command=adv_value.get);rad_adv["2"].grid(column=1,row=0)
#endregion

line = tk.Frame(Part2,background="#E4E4E4",height=10)
line.pack(fill="x")

# show zone now
wrapper_zone.pack(fill="both",expand=1)
#endregion

#region PART 3

#region on_focus
def on_focus_profile(event):
    if event.widget == Part3 and not get_user():
        user_portal()

Part3.bind("<FocusIn>", on_focus_profile)
#endregion

#region info widget
name_widget = ttk.Label(Part3,name="pseudo", text="")
name_widget.grid(column=1,row=0)
gender_widget = ttk.Label(Part3,name="gender", text="")
gender_widget.grid(column=1,row=1)
age_widget = ttk.Label(Part3,name="age",text="")
age_widget.grid(column=1,row=2)
pdp_favorite = tk.Frame(Part3,name="pdp",width=100,height=100)
pdp_favorite.grid(column=0,row=0,rowspan=3)
favorite_widget = tk.Label(Part3,name="favorite",text="",background="grey")
favorite_widget.grid(column=0,row=0,rowspan=3)

btn_edit = ttk.Button(Part3,text="edit profil",command=edit_user)
btn_edit.grid(column=0,row=4)
btn_disc = ttk.Button(Part3,text="disconnect",command=disconnect)
btn_disc.grid(column=1,row=4)
btn_delt = ttk.Button(Part3,text="delete account",command=delete_user)
btn_delt.grid(column=2,row=4)
#endregion
#endregion

#region PART 4

def user_add_book(event):
    if event.widget == Part4:
        try:
            edit_book(True)
        except tk.TclError:
            WINDOW.nametowidget('book_adding').focus_set()

Part4.bind("<FocusIn>", user_add_book)
#endregion

#region close all windows open and task
def on_closing():
    if msg.askokcancel("Quit", "Do you want to quit?"):
        WINDOW.destroy()
        sys.exit()

WINDOW.protocol("WM_DELETE_WINDOW", on_closing)
#endregion

# run the app
WINDOW.mainloop()