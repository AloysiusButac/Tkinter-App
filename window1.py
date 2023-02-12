import tkinter as tk
# from tkinter import ttk
# from tkinter import Button
from PIL import Image,ImageTk

class Window1():
    button_font = ("Arial", 14)

    def __init__(self, parent, title = "Window 1", width = 1000, height = 600):
        self.root = parent
        window_w = width
        window_h = height
        if isinstance(parent, tk.Tk):
            pos_x = (self.root.winfo_screenwidth() // 2) - (window_w // 2)
            pos_y = (self.root.winfo_screenheight() // 2) - (window_h // 2) - 50
            self.root.geometry('{}x{}+{}+{}'.format(window_w, window_h, pos_x, pos_y))
            self.root.title(title)
            self.root.resizable(0, 0)

        # Main Widow Frames
        container_frame = tk.Frame(self.root)
        display_frame = tk.Frame(container_frame)
        ui_frame = tk.Frame(container_frame)

        container_frame.columnconfigure(0, weight=3)
        container_frame.columnconfigure(1, weight=1, minsize=300)
        container_frame.rowconfigure(0, weight=1)

        # Display Frame setup
        display_frame.columnconfigure(0, weight=1)
        display_frame.columnconfigure(1, weight=1)
        display_frame.rowconfigure(0, weight=1)
        display_frame.rowconfigure(1, weight=1)

        ## Create Canvas grid
        canv1 = tk.Canvas(display_frame, bd=0, relief="solid", highlightbackground="#aaa", highlightthickness=2)
        canv2 = tk.Canvas(display_frame, bd=0, relief="solid", highlightbackground="#aaa", highlightthickness=2)
        canv3 = tk.Canvas(display_frame, bd=0, relief="solid", highlightbackground="#aaa", highlightthickness=2)
        canv4 = tk.Canvas(display_frame, bd=0, relief="solid", highlightbackground="#aaa", highlightthickness=2)
        canv1.grid(column=0, row=0, pady=2, padx=2, stick="news")
        canv2.grid(column=1, row=0, pady=2, padx=2, stick="news")
        canv3.grid(column=0, row=1, pady=2, padx=2, stick="news")
        canv4.grid(column=1, row=1, pady=2, padx=2, stick="news")
        ## Load image on each canvas
        self.img1 = ImageTk.PhotoImage(Image.open("Koala.jpg").resize([500, 500], Image.BILINEAR))
        self.img2 = ImageTk.PhotoImage(Image.open("Koala.jpg").resize([500, 500], Image.BILINEAR))
        self.img3 = ImageTk.PhotoImage(Image.open("Koala.jpg").resize([500, 500], Image.BILINEAR))
        self.img4 = ImageTk.PhotoImage(Image.open("Koala.jpg").resize([500, 500], Image.BILINEAR))
        ## Add image on each canvas
        canv1.create_image(0, 0, anchor=tk.NW, image=self.img2)
        canv2.create_image(0, 0, anchor=tk.NW, image=self.img2)
        canv3.create_image(0, 0, anchor=tk.NW, image=self.img3)
        canv4.create_image(0, 0, anchor=tk.NW, image=self.img4)

        # UI Frame setup
        self.btn1 = tk.Button(ui_frame, text="NOTIFICATION", font=self.button_font, bd=1, relief="solid", foreground="#333", command=self.ShowNotification) 
        self.btn2 = tk.Button(ui_frame, text="HISTORY", font=self.button_font, bd=1, relief="solid", foreground="#333", command=self.ShowHistory)
        self.btn3 = tk.Button(ui_frame, text="MENU", font=self.button_font, bd=1, relief="solid", foreground="#333", command=self.ShowMenu)

        self.btn1.pack(padx=2, pady=2, ipadx=20, side="top", fill=tk.X)
        self.btn2.pack(padx=2, pady=2, ipadx=20, side="top", fill=tk.X)
        self.btn3.pack(padx=2, pady=2, ipadx=20, anchor="e", side="bottom")

        #  Window Frames Deployment
        container_frame.pack(padx=10, pady=10, fill="both", expand=True)
        display_frame.grid(column=0, row=0, padx=20, pady=20, sticky="nw")
        ui_frame.grid(column=1, row=0, padx=10, pady=30, sticky="news")

    def show(self):
        self.root.mainloop()
    def ShowNotification(self):
        pass
    def ShowHistory(self):
        pass
    def ShowMenu(self):
        pass