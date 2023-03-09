import cv2
import tkinter as tk
from tkinter.ttk import Separator, Style
from PIL import ImageTk, Image

class Util:
    def __init__(self, parent, title="", bg="white", font="Arial 14"):
        super().__init__(parent)
    
    def CreateNotificationPill(self, parent, imgpath="", title="title", message="Nettification message", width=500, height=100, font=None, side="top"):
        container = tk.Frame(parent, bd=2)
        lbl_message = tk.Label(container, text="{}: {}".format(title, message))
        lbl_message.pack(padx=20, pady=0, side=side)

        return container

    def CreateHistoryPill(parent, imgpath="", title="title", width=500, height=100, font=None, side="top"):
        container = tk.Frame(parent, bd=2)
        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=10)
        container.rowconfigure(0, weight=1)
        lbl_message = tk.Label(container, text="{}".format(title))
        canv = tk.Canvas(container, height=40, width=40, bd=0, highlightbackground="#222", highlightthickness=2)
        
        lbl_message.grid(padx=20, column=1, row=0, sticky="news")
        canv.grid(padx=10, column=0, row=0, sticky="news")

        return container

    def ScaleDimensions(dim1=(338, 266), dim2=(704, 540)):
        m = dim2[0] / dim1[0]
        n = dim2[1] / dim1[1]
        if (m < n):
            return (int(dim1[0] * m), int(dim1[1] * m))
        else:
            return (int(dim1[0] * n), int(dim1[1] * n))

    def rescale_frame(frame, percent=75):
        width = int(frame.shape[1] * percent/ 100)
        height = int(frame.shape[0] * percent/ 100)
        dim = (width, height)
        return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

    def CreateStatPill(parent, image, title="Pill", width=500, height=50, font=None, value=""):
        container = tk.Frame(parent, bg="#fff", bd=2, highlightbackground="#222", highlightthickness=1)
        lbl = tk.Label(container, text=title, font=("Arial 12"), bg="#fff")
        canv = tk.Canvas(container, height=50, width=50, bd=0, bg="#fff", highlightbackground="#222", highlightthickness=0)

        canv.create_image(0, 0, anchor=tk.NW, image=image)
        
        canv.pack(padx=2, pady=2, side="left")
        lbl.pack(padx=20, pady=0, side="left")
        return container

    def CreateDataPill(parent, image, title="Pill", width=500, height=100, font=None, side="top"):
        container = tk.Frame(parent, highlightbackground="#222", highlightthickness=1, bg="#fff")
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)
        container.rowconfigure(1, weight=1)

        lbl = tk.Label(container, text=title, font=("Arial 12"), bg="#fff")
        canv = tk.Canvas(container, height=height, width=width, bg="#fff", highlightbackground="#fff")

        canv.create_image(width//2, height//2, anchor=tk.CENTER, image=image)
        
        lbl.grid(column=0, row=0, padx=20, pady=0, sticky="nw")
        canv.grid(column=0, row=1, padx=2, pady=2, sticky="nw")

        return container

    def CreateButtonArray(parent, count=0, titles=[], commands=[], anchor="left"):
        output = []
        for i in range(count):
            output.append(tk.Button(parent, text=titles[i], font=("Arial 12"), bd=1, bg="#fff", relief="solid", foreground="#333"))
        return output
