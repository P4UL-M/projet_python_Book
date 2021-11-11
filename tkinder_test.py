import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as stxt
import tkinter.messagebox as msg
import tkinter.filedialog as tkfile

window = tk.Tk()

window.title("Welcome to our Book app")
window.geometry('800x600')


tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='First')
tab_control.add(tab2, text='Second')

tab_control.pack(expand=1, fill='both')

lbl = tk.Label(tab1, text="Hello Word",font=("Arial Bold", 50))

lbl.grid(column=0, row=0)

def clicked():
    lbl.configure(text=f"Button was clicked !!{txt.get()}")
    msg.showinfo('Message title','Message content')


btn = tk.Button(tab1, text="Click Me",command=clicked)

btn.grid(column=0, row=2)

txt = tk.Entry(tab1,width=10)

txt.grid(column=0, row=1)

txt.focus()

combo = ttk.Combobox(tab1)

combo['values']= (1, 2, 3, 4, 5, 6)

combo.current(1)

combo.grid(column=0, row=3)

chk = ttk.Checkbutton(tab1, text='Choose')

chk.grid(column=0, row=4)

rad1 = ttk.Radiobutton(tab1,text='First', value=1)
rad2 = ttk.Radiobutton(tab1,text='Second', value=2)

rad1.grid(column=0, row=5)
rad2.grid(column=1,row=5)

txt2 = stxt.ScrolledText(tab1,width=40,height=10)
txt2.grid(column=0,row=6)


#msg.showwarning('Message title', 'Message content')  #shows warning message

#msg.showerror('Message title', 'Message content')    #shows error message

res = msg.askyesno('Message title','Message content')

spin = tk.Spinbox(tab1, from_=0, to=100, width=5)
spin.grid(column=0,row=7)

bar = ttk.Progressbar(tab1, length=200)
bar.grid(column=0,row=8)
bar["value"] = 50


def get_file(): 
    file = tkfile.askopenfilename()

menu = tk.Menu(tab1)

new_item = tk.Menu(menu)

new_item.add_command(label='New',command=get_file)

menu.add_cascade(label='File', menu=new_item)

window.config(menu=menu)

window.mainloop()