import tkinter as tk
from PIL import Image,ImageTk
from VideoCapture import *
from tkinter import Toplevel
import cv2

class HistoryWindow:
    def __init__(self, parent):
        self.main_container = tk.Frame(parent, bg="#9bb")

        # =============== Refresh ================
        btn_container = tk.Frame(self.main_container, bg="#9bb")
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
    
    def get_window(self):
        return self.main_container

    def CreateFormalList(self):
        container = tk.Frame(self.main_container, bg="#9bb")
        canv1 = tk.Canvas(container, bg="#9bb")

        lbl_frame = tk.Frame(canv1, bg="#fff")
        lbl_frame.columnconfigure(0, weight=1)
        lbl_frame.columnconfigure(1, weight=1)
        lbl_frame.columnconfigure(2, weight=1)
        lbl_frame.columnconfigure(3, weight=1)
        lbl_frame.columnconfigure(4, weight=1)
        lbl_frame.rowconfigure(0, weight=1)
        lbl = tk.Label(lbl_frame, text="Camera", bg="#fff").grid(column=0, row=0, sticky="news")
        lbl2 = tk.Label(lbl_frame, text="Recording ID", bg="#fff").grid(column=1, row=0, sticky="news")
        lbl3 = tk.Label(lbl_frame, text="Duration", bg="#fff").grid(column=2, row=0, sticky="news")
        lbl4 = tk.Label(lbl_frame, text="Date", bg="#fff").grid(column=3, row=0, sticky="news")
        lbl5 = tk.Label(lbl_frame, text="Title 2", bg="#fff").grid(column=4, row=0, sticky="news")
        lbl_frame.pack(ipadx=0, ipady=0, side="top", fill="x")

        lb = tk.Listbox(canv1, width=128, bd=0, relief="solid")
        lb.pack(side="left", fill="both", expand=True)
        scroll = tk.Scrollbar(canv1)
        scroll.pack(side="right", fill="y")

        for i in range(20):
            lb.insert(tk.END, i)
        
        lb.config(yscrollcommand=scroll.set)
        scroll.config(command=lb.yview)
        canv1.pack(fill="both", expand=True)

        return container
