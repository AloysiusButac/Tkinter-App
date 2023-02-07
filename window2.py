import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

# https://www.activestate.com/resources/quick-reads/how-to-add-images-in-tkinter/
# https://www.c-sharpcorner.com/blogs/basics-for-displaying-image-in-tkinter-python

class Window2():
    def __init__(self, parent, title = "Window 2", width = 800, height = 600):
        root = parent
        window_w = width
        window_h = height
        pos_x = (root.winfo_screenwidth() // 2) - (window_w // 2)
        pos_y = (root.winfo_screenheight() // 2) - (window_h // 2) - 50
        root.geometry('{}x{}+{}+{}'.format(window_w, window_h, pos_x, pos_y))
        root.title(title)
        root.resizable(0, 0)

        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=4, minsize=200)
        root.columnconfigure(2, weight=2)
        root.rowconfigure(0, weight=1, )
        root.rowconfigure(1, weight=1)

        # Sidebar 
        sidebar_frame = tk.Frame(root, bg="yellow")
        sidebar_frame.rowconfigure(0, weight=1)
        sidebar_frame.rowconfigure(1, weight=3)
        sidebar_frame.rowconfigure(2, weight=2)
        ## Image & Buttons
        img = tk.Canvas(sidebar_frame, bg="#999", bd=1, relief="solid")
        btn_container = tk.Frame(sidebar_frame, bg="#aaa", bd=1, relief="solid")
        btn1 = tk.Button(btn_container, text="Button").pack()
        btn2 = tk.Button(btn_container, text="Button").pack()
        btn3 = tk.Button(btn_container, text="Button").pack()
        btn4 = tk.Button(btn_container, text="Button").pack()
        # Connection Status panel
        connection_status_frame = tk.Frame(sidebar_frame, bg="#bbb", bd=1, relief="solid")
        connection_status_frame.rowconfigure(0, weight=1)
        connection_status_frame.rowconfigure(1, weight=1)
        connection_status_frame.rowconfigure(2, weight=1)
        connection_status_frame.columnconfigure(0, weight=1)
        connection_status_frame.columnconfigure(1, weight=1)
        connection_status_frame.columnconfigure(2, weight=1)
        ## Connection Status Elements
        lbl_connstat = tk.Label(connection_status_frame, text="Connection Status:")
        btn_cn1 = tk.Button(connection_status_frame, text="Button")
        btn_cn2 = tk.Button(connection_status_frame, text="Button")
        btn_cn3 = tk.Button(connection_status_frame, text="Button")
        ## Positioning Elements in grid within frame
        img.grid(column=0, row=0, sticky="n")
        btn_container.grid(column=0, row=1, sticky="n")
        lbl_connstat.grid(column=0, row=0, columnspan=3)
        btn_cn1.grid(column=0, row=1, columnspan=3)
        btn_cn2.grid(column=0, row=2, columnspan=2)
        btn_cn3.grid(column=2, row=2)
        connection_status_frame.grid(column=0, row=2, sticky="s")

        # Main Panel
        data_frame = tk.Frame(root, bg="green", bd=1, relief="solid")

        menu = tk.Menu(root)
        root.config(menu=menu)
        fileMenu = tk.Menu(menu)
        fileMenu.add_command(label="About")
        fileMenu.add_command(label="Exit")
        menu.add_cascade(label="File", menu=fileMenu)


        # Positioning frames within window
        sidebar_frame.grid(column=0, row=0, rowspan=2, sticky="news")
        data_frame.grid(column=1, row=0, columnspan=2, rowspan=2, sticky="news")

        root.mainloop()