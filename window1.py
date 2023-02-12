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
        self.maximized_canvas = [0, 0, 0, 0]
        self.canv1 = tk.Canvas(display_frame, bd=0, relief="solid", highlightbackground="#aaa", highlightthickness=2)
        self.canv2 = tk.Canvas(display_frame, bd=0, relief="solid", highlightbackground="#aaa", highlightthickness=2)
        self.canv3 = tk.Canvas(display_frame, bd=0, relief="solid", highlightbackground="#aaa", highlightthickness=2)
        self.canv4 = tk.Canvas(display_frame, bd=0, relief="solid", highlightbackground="#aaa", highlightthickness=2)
        # self.canv1.update()
        # self.canv2.update()
        # self.canv3.update()
        # self.canv4.update()
        self.canvas1_wh = [self.canv1.winfo_width(), self.canv1.winfo_height()]
        self.canvas2_wh = [self.canv2.winfo_width(), self.canv2.winfo_height()]
        self.canvas3_wh = [self.canv3.winfo_width(), self.canv3.winfo_height()]
        self.canvas4_wh = [self.canv4.winfo_width(), self.canv4.winfo_height()]
        self.canv1.bind("<Button-1>", lambda event: 
            self.focusOnCamera(event, 1)
        )
        self.canv2.bind("<Button-1>", lambda event:
            self.focusOnCamera(event, 2)
        )
        self.canv3.bind("<Button-1>", lambda event:
            self.focusOnCamera(event, 3)
        )
        self.canv4.bind("<Button-1>", lambda event: 
            self.focusOnCamera(event, 4)
        )
        print(self.canvas1_wh[0], self.canvas1_wh[1])
        print(self.canvas2_wh[0], self.canvas2_wh[1])
        print(self.canvas3_wh[0], self.canvas3_wh[1])
        print(self.canvas4_wh[0], self.canvas4_wh[1])
        self.canv1.grid(column=0, row=0, pady=2, padx=2, stick="news")
        self.canv2.grid(column=1, row=0, pady=2, padx=2, stick="news")
        self.canv3.grid(column=0, row=1, pady=2, padx=2, stick="news")
        self.canv4.grid(column=1, row=1, pady=2, padx=2, stick="news")
        ## Load image on each canvas
        self.img1 = ImageTk.PhotoImage(Image.open("video.png").resize([280, 280], Image.BILINEAR))
        # self.image2 = ImageTk.PhotoImage(Image.open("video.png").resize([500, 500], Image.BILINEAR))
        # self.img2 = ImageTk.PhotoImage(Image.open("Koala.jpg").resize([500, 500], Image.BILINEAR))
        # self.img3 = ImageTk.PhotoImage(Image.open("Koala.jpg").resize([500, 500], Image.BILINEAR))
        # self.img4 = ImageTk.PhotoImage(Image.open("Koala.jpg").resize([500, 500], Image.BILINEAR))
        ## Add image on each canvas
        self.canv1_image_container = self.canv1.create_image(0, 0, anchor=tk.NW, image=self.img1)
        self.canv2_image_container = self.canv2.create_image(0, 0, anchor=tk.NW, image=self.img1)
        self.canv3_image_container = self.canv3.create_image(0, 0, anchor=tk.NW, image=self.img1)
        self.canv4_image_container = self.canv4.create_image(0, 0, anchor=tk.NW, image=self.img1)

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
    def callback(self, event):
        print("clicked at (" , event.x , ", " , event.y , ")")

    def swapCanvasImage(self, event, image_container=0):
        # setting images
        if image_container == 1:
            self.canv1.itemconfig(self.canv1_image_container, image=self.image2)
        elif image_container == 2:
            self.canv2.itemconfig(self.canv2_image_container, image=self.image2)
        elif image_container == 3:
            self.canv3.itemconfig(self.canv3_image_container, image=self.image2)
        elif image_container == 4:
            self.canv4.itemconfig(self.canv4_image_container, image=self.image2)
        else:
            print("Swap image not working.")
            return
        
        # swap images and 2 
        tmp = self.image2
        self.image2 = self.img1
        self.img1 = tmp

    def focusOnCamera(self, event, cam_num=0):
        if cam_num == 1:
            if self.maximized_canvas[0] == 0:
                self.maximizeCanvas(event, 1)
                self.maximized_canvas[0] = 1
            else:
                self.minimizeCanvas(event, 1)
                self.maximized_canvas[0] = 0
        elif cam_num == 2:
            if self.maximized_canvas[1] == 0:
                self.maximizeCanvas(event, 2)
                self.maximized_canvas[1] = 1
            else:
                self.minimizeCanvas(event, 2)
                self.maximized_canvas[1] = 0
        elif cam_num == 3:
            if self.maximized_canvas[2] == 0:
                self.maximizeCanvas(event, 3)
                self.maximized_canvas[2] = 1
            else:
                self.minimizeCanvas(event, 3)
                self.maximized_canvas[2] = 0
        elif cam_num == 4:
            if self.maximized_canvas[3] == 0:
                self.maximizeCanvas(event, 4)
                self.maximized_canvas[3] = 1
            else:
                self.minimizeCanvas(event, 4)
                self.maximized_canvas[3] = 0
        else:
            print("focus on cam not working.", cam_num)
            return

    def maximizeCanvas(self, event, canvas_num=0):
        if canvas_num == 1:
            self.canv1.config(width=1100, height=900)
            # self.canv2.itemconfig(1,state="hidden")
            # self.canv3.itemconfig(1,state="hidden")
            # self.canv4.itemconfig(1,state="hidden")
        elif canvas_num == 2:
            self.canv2.config(width=1100, height=900)
            # self.canv1.itemconfig(1,state="hidden")
            # self.canv3.itemconfig(1,state="hidden")
            # self.canv4.itemconfig(1,state="hidden")
        elif canvas_num == 3:
            self.canv3.config(width=1100, height=900)
            # self.canv4.itemconfig(1,state="hidden")
            # self.canv2.itemconfig(1,state="hidden")
            # self.canv1.itemconfig(1,state="hidden")
        elif canvas_num == 4:
            self.canv4.config(width=1100, height=900)
            # self.canv3.itemconfig(1,state="hidden")
            # self.canv2.itemconfig(1,state="hidden")
            # self.canv1.itemconfig(1,state="hidden")
        else:
            print("maximize canvas not working.", canvas_num)
            return

    def minimizeCanvas(self, event, canvas_num=0):
        if canvas_num == 1:
            self.canv1.config(width=300, height=300)
            # self.canv2.itemconfig(1,state="normal")
            # self.canv3.itemconfig(1,state="normal")
            # self.canv4.itemconfig(1,state="normal")
        elif canvas_num == 2:
            self.canv2.config(width=300, height=300)
            # self.canv1.itemconfig(1,state="normal")
            # self.canv3.itemconfig(1,state="normal")
            # self.canv4.itemconfig(1,state="normal")
        elif canvas_num == 3:
            self.canv3.config(width=300, height=300)
            # self.canv4.itemconfig(1,state="normal")
            # self.canv2.itemconfig(1,state="normal")
            # self.canv1.itemconfig(1,state="normal")
        elif canvas_num == 4:
            self.canv4.config(width=300, height=300)
            # self.canv3.itemconfig(1,state="normal")
            # self.canv2.itemconfig(1,state="normal")
            # self.canv1.itemconfig(1,state="normal")
        else:
            print("minimize canvas not working.", canvas_num)
            return
