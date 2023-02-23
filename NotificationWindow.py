import tkinter as tk
from PIL import Image,ImageTk
from VideoCapture import *
from tkinter import Toplevel
import cv2

class NotificationWindow():
    button_font = ("Arial", 14)

    def __init__(self, parent, title = "Notification Window", width = 1000, height = 600):
        container = tk.Frame(self.NotificationWindow)

        canvas = tk.Canvas(container)
        frame = tk.Frame(canvas)
        scroll = tk.Scrollbar(self.NotificationWindow, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scroll.set)

        self.label_list = [tk.Label(container, text="Label")] * 10

        for lbl in len(self.label_list):
            lbl.pack(padx=10, pady=5, stick="news")

        scroll.pack(side="right", fill="y")
        canvas.pack(side="left")
        canvas.create_window((0,0), window=frame, anchor="nw")
        frame.bind("<Configure>", lambda event : canvas.configure(scrollregion=canvas.bbox("all"), width = 300, height=300))

        container.pack(fill="both", expand=True)
    
    def show():
        self.root.mainloop()
