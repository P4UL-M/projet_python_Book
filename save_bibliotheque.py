import tkinter as tk
import tkinter.ttk as ttk


def get_connection(master:tk.Frame):
    win = tk.Tk()
    win.geometry("343x122")
    
    win.title("Connection portal")
    win.focus_force()

    main = ttk.Frame(win)
    main.pack(fill="both",expand=1)

    def on_focus_out(event):
        if event.widget == win:
            print(dir(event))
            win.focus_force()

    def on_closing():
        master.focus_set()
    
    center = ttk.Frame(main)
    center.place(relx=0.5, rely=0.5, anchor="center")
    name = ttk.Entry(center)
    name.grid(column=0,row=0)
    btn = ttk.Button(center,text="Connect")
    btn.grid(column=0,row=1,sticky="we")

    win.bind("<FocusOut>", on_focus_out)
    win.protocol("WM_DELETE_WINDOW", on_closing)