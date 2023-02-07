import tkinter as tk
from tkinter import ttk

button_font = ("Arial", 14)

class Window1():
    def __init__(self, parent, title = "Window 1", width = 800, height = 600):
        root = parent
        window_w = width
        window_h = height
        pos_x = (root.winfo_screenwidth() // 2) - (window_w // 2)
        pos_y = (root.winfo_screenheight() // 2) - (window_h // 2) - 50
        root.geometry('{}x{}+{}+{}'.format(window_w, window_h, pos_x, pos_y))
        root.title(title)
        root.resizable(0, 0)


        # Main Widow Frames
        container_frame = tk.Frame(root)
        display_frame = tk.Frame(container_frame)
        ui_frame = tk.Frame(container_frame)
        # container_frame = tk.Frame(root, bg="cyan")
        # display_frame = tk.Frame(container_frame, bg="green")
        # ui_frame = tk.Frame(container_frame, bg="blue")

        container_frame.columnconfigure(0, weight=1)
        container_frame.rowconfigure(0, weight=7)
        container_frame.rowconfigure(1, weight=7)
        container_frame.rowconfigure(2, weight=2, minsize=50)

        # Display Frame setup
        display_frame.columnconfigure(0, weight=1)
        display_frame.columnconfigure(1, weight=1)
        display_frame.rowconfigure(0, weight=1)
        display_frame.rowconfigure(1, weight=1)

        canv1 = tk.Canvas(display_frame, bd=1, relief="solid")
        canv2 = tk.Canvas(display_frame, bd=1, relief="solid")
        canv3 = tk.Canvas(display_frame, bd=1, relief="solid")
        canv4 = tk.Canvas(display_frame, bd=1, relief="solid")

        canv1.grid(column=0, row=0, pady=2, padx=2, stick="nw")
        canv2.grid(column=1, row=0, pady=2, padx=2, stick="ne")
        canv3.grid(column=0, row=1, pady=2, padx=2, stick="sw")
        canv4.grid(column=1, row=1, pady=2, padx=2, stick="se")

        # UI Frame setup
        btn1 = tk.Button(ui_frame, text="Button", font=button_font)
        btn2 = tk.Button(ui_frame, text="Button", font=button_font)
        btn3 = tk.Button(ui_frame, text="Button", font=button_font)

        btn1.pack(padx=2, pady=2, ipadx=20, side="left")
        btn2.pack(padx=2, pady=2, ipadx=20, side="left")
        btn3.pack(padx=2, pady=2, ipadx=20, side="right")

        #  Window Frames Deployment
        container_frame.pack(padx=10, pady=10, fill="both")
        display_frame.grid(column=0, row=0, rowspan=2, padx=40, pady=2, sticky="news")
        ui_frame.grid(column=0, row=2, padx=40, pady=2, sticky="news")

        root.mainloop()