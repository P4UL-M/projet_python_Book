import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as stxt
import tkinter.messagebox as msg
import tkinter.filedialog as tkfile

from dico_tkinder import get_horizontale_scroll_bar

window = tk.Tk()

window.title("Welcome to our Book app")
window.geometry('800x600')

tab_control = ttk.Notebook(window)
#region onglet menu
# create the 3 tabs and add it to the tab_control
Part1 = ttk.Frame(tab_control); tab_control.add(Part1, text='Part 1')
Part2 = ttk.Frame(tab_control); tab_control.add(Part2, text='Part 2')
Part3 = ttk.Frame(tab_control); tab_control.add(Part3, text='Part 3')

# organisation of the tabs
tab_control.pack(expand=1, fill='both')
#endregion

#region PART 1
#region confingscroll bar main
wrapper1 = tk.Frame(Part1)

mycanvas = tk.Canvas(wrapper1,background="black")
tk.Grid.rowconfigure(wrapper1, 0, weight=1)
tk.Grid.columnconfigure(wrapper1, 0, weight=1)
mycanvas.grid(column=0,row=0,sticky='news')

yscrollbar = ttk.Scrollbar(wrapper1,orient=tk.VERTICAL,command=mycanvas.yview)
yscrollbar.grid(column=1,row=0,sticky='ns')

mycanvas.configure(yscrollcommand=yscrollbar.set)

container_frame = tk.Frame(mycanvas)
container_frame_id = mycanvas.create_window((0,0),window=container_frame,anchor="nw")

def config(e):
    mycanvas.configure(scrollregion = mycanvas.bbox('all'))
    mycanvas.itemconfig(container_frame_id, width = e.width)
def _on_mousewheel(event):
    if not event.state:
        mycanvas.yview_scroll(-event.delta, "units")
def _bound_to_mousewheel(e):
    mycanvas.bind_all("<MouseWheel>", _on_mousewheel)
def _unbound_to_mousewheel(e):
    mycanvas.unbind_all("<MouseWheel>")

mycanvas.bind('<Configure>',config)
container_frame.bind('<Enter>', _bound_to_mousewheel)
container_frame.bind('<Leave>', _unbound_to_mousewheel)

wrapper1.pack(fill='both',expand=1,padx=10,pady=10)
#endregion

#region RECOMMENDATION
container_recommandation = tk.Frame(container_frame)
container_recommandation.pack(expand=1,fill="x")
lbl = tk.Label(container_recommandation, text="RECOMMANDATION :",font=("Arial Bold", 25),pady="15",padx="15")
lbl.pack(side="top", anchor="w")

#region configscroll bar recommandation
wrapper2 = tk.Frame(container_recommandation,background="blue")

_frame_scrollable = get_horizontale_scroll_bar(wrapper2)
_frame = _frame_scrollable["frame"]

wrapper2.pack(side=tk.TOP,fill='x',expand=1)
#endregion


gallery_recommandation = {}
color = ["red","blue","yellow","green","brown"]

for i in range(100):
    book = f"book{str(i)}"
    gallery_recommandation[book] = tk.Frame(_frame,height=180,width=100,background=color[i%5])
    _pad = tk.Frame(_frame,width=25)
    _pad.pack(side="left")
    gallery_recommandation[book].pack(side="left",expand=1,fill="x")
    _pad = tk.Frame(_frame,width=25)
    _pad.pack(side="left")
#endregion

#region News
container_news= tk.Frame(container_frame)
container_news.pack(expand=1,fill="x")
lbl = tk.Label(container_news, text="NEWS :",font=("Arial Bold", 25),pady="5",padx="15")
lbl.pack(side="top", anchor="w")

#region configscroll bar News
wrapper3 = tk.Frame(container_news,background="blue")

_frame_scrollable = get_horizontale_scroll_bar(wrapper3)
_frame2 = _frame_scrollable["frame"]

wrapper3.pack(side=tk.TOP,fill='x',expand=1)
#endregion


gallery_news = {}
color = ["red","blue","yellow","green","brown"]

for i in range(100):
    book = f"book{str(i)}"
    gallery_news[book] = tk.Frame(_frame2,height=180,width=100,background=color[i%5])
    _pad = tk.Frame(_frame2,width=25)
    _pad.pack(side="left")
    gallery_news[book].pack(side="left",expand=1,fill="x")
    _pad = tk.Frame(_frame2,width=25)
    _pad.pack(side="left")
#endregion

#region Friends
container_friend= tk.Frame(container_frame)
container_friend.pack(expand=1,fill="x")
lbl = tk.Label(container_friend, text="FRIENDS :",font=("Arial Bold", 25),pady="5",padx="15")
lbl.pack(side="top", anchor="w")
_frame = tk.Frame(container_friend)
_frame.pack(side="top",expand=1,fill="x")

gallery_news = {}
color = ["red","blue","yellow","green","brown"]

for i in range(5):
    book = f"book{str(i)}"
    gallery_news[book] = tk.Frame(_frame,height=180,width=100,background=color[i])
    _pad = tk.Frame(_frame,width=25)
    _pad.pack(side="left")
    gallery_news[book].pack(side="left",expand=1,fill="x")
    _pad = tk.Frame(_frame,width=25)
    _pad.pack(side="left")
#endregion

#region RATE
container_rate= tk.Frame(container_frame)
container_rate.pack(expand=1,fill="x")
lbl = tk.Label(container_rate, text="RATE :",font=("Arial Bold", 25),pady="5",padx="15")
lbl.pack(side="top", anchor="w")
_frame = tk.Frame(container_rate)
_frame.pack(side="top",expand=1,fill="x")

gallery_news = {}
color = ["red","blue","yellow","green","brown"]

for i in range(5):
    book = f"book{str(i)}"
    gallery_news[book] = tk.Frame(_frame,height=180,width=100,background=color[i])
    _pad = tk.Frame(_frame,width=25)
    _pad.pack(side="left")
    gallery_news[book].pack(side="left",expand=1,fill="x")
    _pad = tk.Frame(_frame,width=25)
    _pad.pack(side="left")
#endregion

#endregion

#region PART 2

#endregion

#region PART 3

#endregion

#region Menu déroulant
menu = tk.Menu(Part1)

new_item = tk.Menu(menu)

new_item.add_command(label='New',command=None)

menu.add_cascade(label='File', menu=new_item)

window.config(menu=menu)
#endregion

# run the app
window.mainloop()