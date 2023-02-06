import tkinter as tk
from tkinter import ttk

class Window1(tk.Tk):
    def __init__(self, parent, width = 800, height = 600):
        root = parent
        window_w = width
        window_h = height
        window_title = 'Window 1'
        pos_x = root.winfo_screenwidth() // 2 - (window_w // 2)
        pos_y = root.winfo_screenheight() // 2 - (window_h // 2)
        root.geometry('{}x{}+{}+{}'.format(window_w, window_h, pos_x, pos_y))
        root.title(window_title)
        root.resizable(0, 0)

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=10)
        root.rowconfigure(1, weight=1)

        display_frame = tk.Frame(root, bg="green")
        ui_frame = tk.Frame(root, bg="red")

        ui_frame.columnconfigure(0, weight=2)
        ui_frame.columnconfigure(1, weight=8)
        ui_frame.columnconfigure(2, weight=1)

        btn1 = tk.Button(ui_frame, text="Button")
        btn2 = tk.Button(ui_frame, text="Button")
        btn3 = tk.Button(ui_frame, text="Button")

        btn1.grid(column=0, row=0, padx=10, pady=10, sticky="w")
        btn2.grid(column=0, row=0, padx=10, pady=10, sticky="e")
        btn3.grid(column=2, row=0, padx=10, pady=10 ,sticky="e")

        display_frame.grid(column=0, row=0, sticky="news")
        ui_frame.grid(column=0, row=1, ipadx=10, ipady=10, sticky="news")

        lbl1 = tk.Label(display_frame, text="test1")
        lbl2 = tk.Label(ui_frame, text="test2")


        root.mainloop()