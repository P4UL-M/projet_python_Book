import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import tkinter.filedialog as tkfile
import sys

from lib.preset_widget import *
from lib.preset_fonction_IHM import *

window = tk.Tk()

window.title("Welcome to our Book app")
window.geometry('800x600')

tab_control = ttk.Notebook(window)
#region onglet menu
# create the 3 tabs and add it to the tab_control
Part1 = ttk.Frame(tab_control); tab_control.add(Part1, text='For you')
Part2 = ttk.Frame(tab_control); tab_control.add(Part2, text='Search')
Part3 = ttk.Frame(tab_control); tab_control.add(Part3, text='My Account')

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

recommendation_gallery = get_gallery(wrapper_rec,_frame_scrollable_main,window)

wrapper_rec.pack(side=tk.TOP,fill='x',expand=1)
#endregion

for i in range(10):
    book = {
        "name":f"book{str(i)}",
        "frame":tk.Frame(recommendation_gallery["frame"],height=180,width=100,background="black")
        }
    recommendation_gallery["__add_panel__"](book,recommendation_gallery)
#endregion

#region News
container_new = ttk.Frame(_frame_main)
container_new.pack(expand=1,fill="x")
lbl = ttk.Label(container_new, text="RECENTLY ADDED :",font=("Arial Bold", 25),padding=15)
lbl.pack(side="top", anchor="w")

#region configscroll bar News
wrapper_new = ttk.Frame(container_new)

new_gallery = get_gallery(wrapper_new,_frame_scrollable_main,window)

wrapper_new.pack(side=tk.TOP,fill='x',expand=1)
#endregion

for i in range(10):
    book = {
        "name":f"book{str(i)}",
        "frame":tk.Frame(new_gallery["frame"],height=180,width=100,background="red")
        }
    new_gallery["__add_panel__"](book,new_gallery)
#endregion

#region Friends
container_friend = ttk.Frame(_frame_main)
container_friend.pack(expand=1,fill="x")
lbl = ttk.Label(container_friend, text="YOUR FRIEND ALSO LIKED TO READ :",font=("Arial Bold", 25),padding=15)
lbl.pack(side="top", anchor="w")

#region configscroll bar News
wrapper_friend = ttk.Frame(container_friend)

friend_gallery = get_gallery(wrapper_friend,_frame_scrollable_main,window)

wrapper_friend.pack(side=tk.TOP,fill='x',expand=1)
#endregion

for i in range(10):
    book = {
        "name":f"book{str(i)}",
        "frame":tk.Frame(friend_gallery["frame"],height=180,width=100,background="blue")
        }
    friend_gallery["__add_panel__"](book,friend_gallery)
#endregion

#region RATE
container_rate = ttk.Frame(_frame_main)
container_rate.pack(expand=1,fill="x")
lbl = ttk.Label(container_rate, text="YOU MAYBE WANT TO RATE :",font=("Arial Bold", 25),padding=15)
lbl.pack(side="top", anchor="w")

#region configscroll bar News
wrapper_rate = tk.Frame(container_rate,background="blue")

rate_gallery = get_gallery(wrapper_rate,_frame_scrollable_main,window)

wrapper_rate.pack(side=tk.TOP,fill='x',expand=1)
#endregion

for i in range(10):
    book = {
        "name":f"book{str(i)}",
        "frame":tk.Frame(rate_gallery["frame"],height=180,width=100,background="green")
        }
    rate_gallery["__add_panel__"](book,rate_gallery)
#endregion

#endregion

#region PART 2
frame_search_bar = ttk.Frame(Part2,padding=15)

frame_search_bar.pack(fill="x")

#region Search Bar elts
txt = ttk.Entry(frame_search_bar)
txt.pack(side="left",fill="x",expand=1)
txt.focus()

btn = ttk.Button(frame_search_bar,text="Enter")
btn.pack(side="right")
#endregion

adv_param = get_foldable_frame(Part2,window,text="Advanced settings")
adv_param["frame"].pack(anchor="w")

#region Adv param elt
param1 = ttk.Label(adv_param["sub_frame"],text="this is an advanced parameter")
param1.grid(column=0,row=0)
#endregion

line = tk.Frame(Part2,background="#E4E4E4",height=10)
line.pack(fill="x")

#region results
wrapper_zone = tk.Frame(Part2,background="red")

zone = get_vertical_scroll_bar(wrapper_zone)
for i in range(100):
    get_result_book(zone["frame"],"test",1).pack(fill="x")


wrapper_zone.pack(fill="both",expand=1)
#endregion

"""
Search bar
avanced research
result with a scrollable frame : Book or User, open in new windows
Book page have title, genre, resumé, global rating, comments
User page have name, preferite genre, last read, preferite books,friends

if user is admin add suppress option
"""

#endregion

#region PART 3
def on_focus_profile(event):
    if event.widget == Part3:
        _return = lambda: [f() for f in [lambda :tab_control.select(Part1),lambda:Part1.focus_set()]]
        get_connection(Part3,on_close = _return)

Part3.bind("<FocusIn>", on_focus_profile)

"""

Make the connection here, if not connected open a pop up windows to connect, this fonction could be execute every time we want to make a action that need to be connected

- name
- gender
- age
- preferate genre
-> preferate book
- last read
-> book to rate 
"""


#endregion

#region Menu déroulant
menu = tk.Menu(window)

new_item = tk.Menu(menu)
page_command = lambda: get_connection(window,on_close = lambda: [f() for f in [lambda :tab_control.select(Part1),lambda:Part1.focus_set()]])
new_item.add_command(label='Page',command=page_command)
new_item.add_command(label='Friend',command=None)
new_item.add_command(label='Edit',command=None)
new_item.add_command(label='Disconnect',command=None)
menu.add_cascade(label='Account', menu=new_item)

new_item = tk.Menu(menu)
new_item.add_command(label='Reset my data',command=None)
new_item.add_command(label='Toggle Admin mode',command=None)
new_item.add_command(label='Edit',command=None)
menu.add_cascade(label='Preference', menu=new_item)

new_item = tk.Menu(menu)
new_item.add_command(label='Actual',command=None)
new_item.add_command(label='For you',command=None)
new_item.add_command(label='Search',command=None)
new_item.add_command(label='My Account',command=None)
new_item.add_command(label='Book details',command=None)
new_item.add_command(label='User details',command=None)
menu.add_cascade(label='Aide', menu=new_item)

window.config(menu=menu)
#endregion

#region close all windows open and task
def on_closing():
    if msg.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
        sys.exit()

window.protocol("WM_DELETE_WINDOW", on_closing)
#endregion

# run the app
window.mainloop()