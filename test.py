from tkinter import *
from tkinter import *
from tkinter import ttk

win = Tk()

wrapper1 = LabelFrame(win,background="black")
wrapper2 = LabelFrame(win)

mycanvas = Canvas(wrapper1)
Grid.rowconfigure(wrapper1, 0, weight=1)
Grid.columnconfigure(wrapper1, 0, weight=1)
mycanvas.grid(column=0,row=0,sticky='news')

yscrollbar = ttk.Scrollbar(wrapper1,orient=VERTICAL,command=mycanvas.yview)
yscrollbar.grid(column=1,row=0,sticky='ns')

mycanvas.configure(yscrollcommand=yscrollbar.set)

mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))

myframe = Frame(mycanvas)
mycanvas.create_window((0,0),window=myframe,anchor="nw")

wrapper1.pack(fill='both',expand=1,padx=10,pady=10)
wrapper2.pack(fill='both',expand=1,padx=10,pady=10)

for i in range(50):
    Button(myframe,text="My Button - "+str(i)).pack()


win.geometry("500x500")
win.resizable(False,False)
win.title("test")
win.mainloop()