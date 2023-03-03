import tkinter as tk
from PIL import Image,ImageTk
from VideoCapture import *
# from tkinter import Toplevel
# from tkinter import ttk
from tkinter import *
from tkinter import ttk
import cv2

class NotificationWindow:
    header_font_bold = ("Arial", 18, "bold")
    def __init__(self, parent):
        self.root = parent
        self.main_container = tk.Frame(parent)

        # =============== Refresh ================
        btn_container = tk.Frame(self.main_container)
        btn_container.columnconfigure(0, weight=2)
        btn_container.columnconfigure(1, weight=2)
        btn_container.columnconfigure(2, weight=2)
        btn_container.columnconfigure(3, weight=1)
        btn_refresh = tk.Button(btn_container, bg="#345", fg="#fff", text="Refresh")
        btn_refresh.grid(column=3, row=0, padx=20, pady=5, ipadx=20, ipady=3, sticky="e")
        btn_container.pack(side="top", fill="both")

        # ================ List 1 ================ 
        container = self.CreateFormalList()
        container.pack(padx=20, pady=5, fill="both", expand=True)

        # ================ List 2 ================ 
        container2 = self.CreateFormalList()
        container2.pack(padx=20, pady=5, fill="both", expand=True)

    
    def get_window(self):
        return self.main_container

    def CreateFormalList(self, command=None):
        container = tk.Frame(self.main_container, bg="#fff")
        canv1 = tk.Canvas(container, bg="#fff")

        lbl_frame = tk.Frame(canv1, bg="#fff")
        lbl_frame.columnconfigure(0, weight=1)
        lbl_frame.columnconfigure(1, weight=1)
        lbl_frame.columnconfigure(2, weight=1)
        lbl_frame.columnconfigure(3, weight=1)
        lbl_frame.columnconfigure(4, weight=1)
        lbl_frame.rowconfigure(0, weight=1)
        lbl = tk.Label(lbl_frame, text="Violation ID", bg="#fff").grid(column=0, row=0, sticky="news")
        lbl2 = tk.Label(lbl_frame, text="Violation Type", bg="#fff").grid(column=1, row=0, sticky="news")
        lbl3 = tk.Label(lbl_frame, text="Area", bg="#fff").grid(column=2, row=0, sticky="news")
        lbl4 = tk.Label(lbl_frame, text="Date", bg="#fff").grid(column=3, row=0, sticky="news")
        lbl5 = tk.Label(lbl_frame, text="Recording Frame", bg="#fff").grid(column=4, row=0, sticky="news")
        lbl_frame.pack(ipadx=0, ipady=0, side="top", fill="x")

        lb = tk.Listbox(canv1, width=128, bd=0, relief="solid")
        lb.pack(side="left", fill="both", expand=True)
        scroll = tk.Scrollbar(canv1)
        scroll.pack(side="right", fill="y")

        for i in range(20):
            lb.insert(tk.END, i)

        # ======== List Double Click Acion ========
        def show_options(self):
            item = lb.curselection()

            tp = Toplevel()
            tp.geometry("{}x{}+{}+{}".format(350, 175, 150, 150))
            tp.title("Confirm Violation")

            list_option = tk.Frame(tp)

            list_option.columnconfigure(0, weight=1)
            list_option.columnconfigure(1, weight=1)
            list_option.columnconfigure(2, weight=1)
            list_option.rowconfigure(0, weight=1)
            list_option.rowconfigure(1, weight=2)
            list_option.rowconfigure(2, weight=2)

            listbox_options = ["Standing", "Walking", "Kicking", "Running", "Intimidating", "Striking"]

            lbl_header = tk.Label(list_option, text="Is the violation {}".format(listbox_options[2]), font="Helvetica 12 bold").grid(column=0, row=0, columnspan=2, sticky="nw")

            lbl = tk.Label(list_option, text = "Confirmation:", font="Helvetica 10").grid(column=0, row=1)

            options = ttk.Combobox(list_option, values=listbox_options)

            options.grid(column=1, row=1)

            btn_watch = tk.Button(list_option, text="Watch Video", font="Helvetica 10", bg="#9bb", bd=0, relief="solid")
            btn_edit = tk.Button(list_option, text="Edit", bg="#345", fg="#fff", width=8, font="Helvetica 10")

            btn_watch.grid(column=2, row=1, padx=10, ipadx=2)
            btn_edit.grid(column=2, row=2, padx=10, ipadx=2)

            list_option.pack(padx=10, pady=10, fill="both", expand=True)


        
        # if command is not None:
        lb.bind('<Double-1>', show_options)
        
        lb.config(yscrollcommand=scroll.set)
        scroll.config(command=lb.yview)
        canv1.pack(fill="both", expand=True)

        return container