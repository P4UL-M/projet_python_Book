import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import sys

from lib.books_functions import books
from lib.users_functions import get_readings
from lib.others_functions import verify_data
from lib.app_function import *
from ect.globals import WINDOW,Matrix

"""
This is the main script of our project
there is all the roots of the GUI in tkinter here
we made region with vs-code for folding code to not loose ourself
"""

tab_control = ttk.Notebook(WINDOW)
#region onglet menu
"""
the app is divided is 4 tabs on the main page to each category
"""
# create the 4 tabs and add it to the tab_control
Part1 = ttk.Frame(tab_control,name="home"); tab_control.add(Part1, text='For you')
Part2 = ttk.Frame(tab_control,name="search"); tab_control.add(Part2, text='Search')
Part3 = ttk.Frame(tab_control,name='profile'); tab_control.add(Part3, text='My Account')
Part4 = ttk.Frame(tab_control,name='add_a_book'); tab_control.add(Part4, text='Add a Book')
# organisation of the tabs
tab_control.pack(expand=1, fill='both')
#endregion

#region PART 1
"""
this is the first page of the app where you can see your recommandation and the last books added or the last books you read
"""
#region confingscroll bar main
"""
this region configure the vertical scroll of the main window
"""
wrapper1 = ttk.Frame(Part1)

_frame_scrollable_main = get_vertical_scroll_bar(wrapper1)
_frame_main = _frame_scrollable_main["frame"]

wrapper1.pack(fill='both',expand=1)
#endregion

#region RECOMMANDATION
"""
this region is the first gallery on screen : the recommandation
"""
container_recommandation = ttk.Frame(_frame_main)
container_recommandation.pack(expand=1,fill="x")
lbl = ttk.Label(container_recommandation, text="RECOMMANDATION :",font=("Arial Bold", 25),padding=15)
lbl.pack(side="top", anchor="w")

#region configscroll bar recommandation
"""
this region configure the vertical scroll of the gallery
"""
wrapper_rec = ttk.Frame(container_recommandation) #the gallery must be store in a Frame

recommendation_gallery = get_gallery(wrapper_rec,_frame_scrollable_main) #preconfig for gallery, store in a dictionary

wrapper_rec.pack(side=tk.TOP,fill='x',expand=1)
#endregion
def update_gallery_Rec():
    """
    this fonction update the book show to the screen in the gallery
    """ 
    if "offset" in recommendation_gallery.keys(): #there is an invible frame add if not enought book are show to screen
        recommendation_gallery["offset"].forget()
    
    for child in recommendation_gallery["frame"].winfo_children(): #we remove all child of the frame to update it again with the new informations
        child.forget()
    
    user = get_user() # we get the session
    if user: # if there are a session we can add recommandation to the user connected
        enum = [get_book(book["name"]) for book in recommand_books(user)] # generation of the dictionary of results

        for book in enum:
            frame = tk.Frame(recommendation_gallery["frame"],height=180,width=100,background=STYLES[book["style"]][1])
            text = tk.Label(frame,text=book["name"],fg=STYLES[book["style"]][2],bg=STYLES[book["style"]][1],wraplength=100)
            book = {
                "name":book["name"],
                "frame":frame,
                "text":text
            }
            recommendation_gallery["__add_panel__"](book,recommendation_gallery) #fonction store to the gallery which add a panel to itself
    
    recommendation_gallery["offset"] = ttk.Frame(recommendation_gallery["canvas"],height=180,border=1) #we add the offset we remove before
    recommendation_gallery["offset"].pack(expand=1,fill="both",side="right")
    
update_gallery_Rec()
#endregion

#region News
"""
this is the same region than before but for news
this gallery don't need the user to be connected so it is a bit less long
"""
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
    """
    his fonction update the news gallery
    """
    if "offset" in new_gallery.keys():
        new_gallery["offset"].forget()
    
    for child in new_gallery["frame"].winfo_children():
        child.forget()

    enum = [i for i in books()][:-11:-1] #this time we take the book list and reverse it to get it in last add form the fist order

    for book in enum:
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
"""
this is the same region than before but for the last read of the user
"""
container_rate = ttk.Frame(_frame_main)
container_rate.pack(expand=1,fill="x")
lbl = ttk.Label(container_rate, text="YOU MAYBE WANT TO READ AGAIN :",font=("Arial Bold", 25),padding=15)
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

        enum = [get_book(int(i)) for i in get_readings(user["name"])][::-1] #this time we itter in the readings of the user by reverse order

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
"""
this fonction actualise the data (and debug the window if you use windows for OS)
"""
def actualise(event):
    if event.widget == Part1:
        update_gallery_Rate()
        update_gallery_News()
        update_gallery_Rec()
        _frame_scrollable_main["refresh"]() #fonction add to gallery and vertical frame with scrollbar to force the refresh on windows
        recommendation_gallery["refresh"]()
        new_gallery["refresh"]()
        rate_gallery["refresh"]()

Part1.bind("<FocusIn>", actualise)
#endregion

#endregion

#region PART 2
"""
this region allow the user to navigate throught the database with a search bar
"""
frame_search_bar = ttk.Frame(Part2,padding=15,name="params")

frame_search_bar.pack(fill="x")

# init zone result before param because we need it but it's pack after
wrapper_zone = tk.Frame(Part2,background="red",name="wrapper")
zone = get_vertical_scroll_bar(wrapper_zone)

func = lambda e=None:generate_result(main_frame=zone) #we create a lanbda because we can't pass personnal argument in event in tkinter (normally useless with class but here we need to do it)

#region Search Bar elts
"""
this region is for the search bar of the 2nd tab
"""
txt = ttk.Entry(frame_search_bar,name="search_bar") 
txt.pack(side="left",fill="x",expand=1)
txt.focus()
txt.bind("<Return>",func) #after initiate the scroll bar we bind the lambda to the enter key

btn = ttk.Button(frame_search_bar,text="Enter",command=func) # the button also triggers the lambda
btn.pack(side="right")
#endregion

adv_param = get_foldable_frame(Part2,WINDOW,text="Advanced settings") #this is a fonction that return a foldable frame
adv_param["frame"].pack(anchor="w")

#region Adv param elt
""""
this region create all teh advanced parameters of the searchbar
"""
rad_adv = dict()
adv_value = tk.StringVar(Part2,name="adv_var")
rad_adv["1"] = ttk.Radiobutton(adv_param["sub_frame"],text='Book',variable=adv_value, value="book",command=adv_value.get);rad_adv["1"].grid(column=0, row=0)
rad_adv["2"] = ttk.Radiobutton(adv_param["sub_frame"],text='User',variable=adv_value, value="user",command=adv_value.get);rad_adv["2"].grid(column=1,row=0)
#endregion

line = tk.Frame(Part2,background="#E4E4E4",height=10) #line of separation between the two elt (color of base widget separator)
line.pack(fill="x")

# show zone now
wrapper_zone.pack(fill="both",expand=1)

#region on_focus
"""
this region update the result when we focus again on the tab so the data stay true
"""
def on_focus_profile(event):
    if event.widget == Part2 and zone["frame"].winfo_children():
        generate_result(main_frame=zone)

Part2.bind("<FocusIn>", on_focus_profile)
#endregion

#endregion

#region PART 3
"""
this region allow the user to connect himself in the 3rd tab to access personnal functionalities
"""
#region on_focus
def on_focus_profile(event):
    """
    every time we bind focus we need to verify if the target is really the tab whose the function was bind
    """
    if event.widget == Part3 and not get_user():
        user_portal() #this function add the user to the tkinter tab so we can access anywhere, session is depedant of the GUI but this allow us access it from any script without any error of unuptated data

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
"""
this region allow the user to add a book to the plateform by clicking on the tab
"""
def user_add_book(event):
    """
    this fonction bind the focus of the tab to the edit of a new book
    """
    if event.widget == Part4:
        try:
            edit_book(True)
        except tk.TclError: #if we already have a window to edit a book we just focus it again
            WINDOW.nametowidget('book_adding').focus_set()

Part4.bind("<FocusIn>", user_add_book)
#endregion

#region close all windows open and task
"""
this region make sure everything stop on the close of the main window
"""
def on_closing():
    if msg.askokcancel("Quit", "Do you want to quit?"):
        WINDOW.destroy()
        sys.exit()

WINDOW.protocol("WM_DELETE_WINDOW", on_closing)
#endregion

# run the app
verify_data() # we verify the data before trying to launch the app so it stop on fatal error in data
generate_matrix() # we must generate the matrix at least one time
print(Matrix)
WINDOW.mainloop() #main loop of tkinter