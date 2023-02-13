import tkinter as tk
from PIL import Image,ImageTk
from VideoCapture import *

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
        self.container_frame = tk.Frame(self.root)
        self.display_frame = tk.Frame(self.container_frame)
        self.display_frame_large = tk.Frame(self.container_frame)
        self.ui_frame = tk.Frame(self.container_frame)

        self.container_frame.columnconfigure(0, weight=3)
        self.container_frame.columnconfigure(1, weight=1, minsize=300)
        self.container_frame.rowconfigure(0, weight=1)

        # Display Frame setup
        self.display_frame.columnconfigure(0, weight=1)
        self.display_frame.columnconfigure(1, weight=1)
        self.display_frame.rowconfigure(0, weight=1)
        self.display_frame.rowconfigure(1, weight=1)

        ## Create Canvas grid
        self.maximized_canvas = [0, 0, 0, 0]
        self.canv1 = tk.Canvas(self.display_frame, bd=0, relief="solid", highlightbackground="#aaa", highlightthickness=2)
        self.canv2 = tk.Canvas(self.display_frame, bd=0, relief="solid", highlightbackground="#aaa", highlightthickness=2)
        self.canv3 = tk.Canvas(self.display_frame, bd=0, relief="solid", highlightbackground="#aaa", highlightthickness=2)
        self.canv4 = tk.Canvas(self.display_frame, bd=0, relief="solid", highlightbackground="#aaa", highlightthickness=2)
        self.canv1.bind("<Button-1>", lambda event: 
            # print("cam 1")
            # self.focusOnCamera(event, 1)
            self.displayCamZoom()
        )
        self.canv2.bind("<Button-1>", lambda event:
            # print("cam 2")
            # self.focusOnCamera(event, 2)
            self.displayCamZoom()
        )
        self.canv3.bind("<Button-1>", lambda event:
            # print("cam 3")
            # self.focusOnCamera(event, 3)
            self.displayCamZoom()
        )
        self.canv4.bind("<Button-1>", lambda event: 
            # print("cam 4")
            # self.focusOnCamera(event, 4)
            self.displayCamZoom()
        )
        self.display_frame.update()
        self.canvas1_wh = [self.canv1.winfo_width(), self.canv1.winfo_height()]
        self.canvas2_wh = [self.canv2.winfo_width(), self.canv2.winfo_height()]
        self.canvas3_wh = [self.canv3.winfo_width(), self.canv3.winfo_height()]
        self.canvas4_wh = [self.canv4.winfo_width(), self.canv4.winfo_height()]
        self.canv1.grid(column=0, row=0, pady=2, padx=2, stick="news")
        self.canv2.grid(column=1, row=0, pady=2, padx=2, stick="news")
        self.canv3.grid(column=0, row=1, pady=2, padx=2, stick="news")
        self.canv4.grid(column=1, row=1, pady=2, padx=2, stick="news")
        ## Load image on each canvas
        self.img1 = ImageTk.PhotoImage(Image.open("video.png").resize([280, 280], Image.BILINEAR))
        ## Add image on each canvas
        self.canv1_image_container = self.canv1.create_image(0, 0, anchor=tk.NW, image=self.img1)
        self.canv2_image_container = self.canv2.create_image(0, 0, anchor=tk.NW, image=self.img1)
        self.canv3_image_container = self.canv3.create_image(0, 0, anchor=tk.NW, image=self.img1)
        self.canv4_image_container = self.canv4.create_image(0, 0, anchor=tk.NW, image=self.img1)

        # Large display setup
        canv_big = tk.Canvas(self.display_frame_large, width=400, height=400, bd=0, relief="solid", highlightbackground="#aaa", highlightthickness=2)
        canv_big.bind("<Button-1>", lambda event : self.displayCamGrid())
        # canv_big.bind("<Button-1>", lambda event : print("big canvas"))
        canv_big.pack(padx=10, pady=10, fill="both", expand=True)

        # UI Frame setup
        self.btn1 = tk.Button(self.ui_frame, text="NOTIFICATION", font=self.button_font, bd=1, relief="solid", foreground="#333", command=self.ShowNotification) 
        self.btn2 = tk.Button(self.ui_frame, text="HISTORY", font=self.button_font, bd=1, relief="solid", foreground="#333", command=self.ShowHistory)
        self.btn3 = tk.Button(self.ui_frame, text="MENU", font=self.button_font, bd=1, relief="solid", foreground="#333", command=self.ShowMenu)

        self.btn1.pack(padx=2, pady=2, ipadx=20, side="top", fill=tk.X)
        self.btn2.pack(padx=2, pady=2, ipadx=20, side="top", fill=tk.X)
        self.btn3.pack(padx=2, pady=2, ipadx=20, anchor="e", side="bottom")

        #  Window Frames Deployment
        self.container_frame.pack(padx=10, pady=10, fill="both", expand=True)
        self.display_frame.grid(column=0, row=0, padx=20, pady=20, sticky="nw")
        self.display_frame_large.grid(column=0, row=0, padx=20, pady=20, sticky="news")
        self.ui_frame.grid(column=1, row=0, padx=10, pady=30, sticky="news")

    def show(self):
        self.root.mainloop()

    def ShowNotification(self):
        pass
    def ShowHistory(self):
        pass
    def ShowMenu(self):
        pass

    def focusOnCamera(self, event, cam_num=0):
        if cam_num == 1:
            if self.maximized_canvas[0] == 0:
                self.displayCamGrid()
                # self.maximizeCanvas(event, 1)
                self.maximized_canvas[0] = 1
            else:
                self.displayCamZoom()
                # self.minimizeCanvas(event, 1)
                self.maximized_canvas[0] = 0
        elif cam_num == 2:
            if self.maximized_canvas[1] == 0:
                self.displayCamGrid()
                # self.maximizeCanvas(event, 2)
                self.maximized_canvas[1] = 1
            else:
                self.displayCamZoom()
                # self.minimizeCanvas(event, 2)
                self.maximized_canvas[1] = 0
        elif cam_num == 3:
            if self.maximized_canvas[2] == 0:
                self.displayCamGrid()
                # self.maximizeCanvas(event, 3)
                self.maximized_canvas[2] = 1
            else:
                self.displayCamZoom()
                # self.minimizeCanvas(event, 3)
                self.maximized_canvas[2] = 0
        elif cam_num == 4:
            if self.maximized_canvas[3] == 0:
                self.displayCamGrid()
                # self.maximizeCanvas(event, 4)
                self.maximized_canvas[3] = 1
            else:
                self.displayCamZoom()
                # self.minimizeCanvas(event, 4)
                self.maximized_canvas[3] = 0
        else:
            print("focus on cam not working.", cam_num)
            return

    ## FIXME: to change image size, delete and load a new image instance Ref: http://www.java2s.com/Code/Python/GUI-Tk/CanvaspaintcontrolledbyScale.htm
    # def maximizeCanvas(self, event, canvas_num=0):
    #     if canvas_num == 1:
    #         self.canv1.config(width=1100, height=900)
    #         self.canv1.scale("all", 0, 0, 2, 2)
    #     elif canvas_num == 2:
    #         self.canv2.config(width=1100, height=900)
    #     elif canvas_num == 3:
    #         self.canv3.config(width=1100, height=900)
    #     elif canvas_num == 4:
    #         self.canv4.config(width=1100, height=900)
    #     else:
    #         print("maximize canvas not working.", canvas_num)
    #         return

    # def minimizeCanvas(self, event, canvas_num=0):
    #     if canvas_num == 1:
    #         self.canv1.config(width=300, height=300)
    #         self.canv1.scale("all", 0, 0, 0.5, 0.5)
    #     elif canvas_num == 2:
    #         self.canv2.config(width=300, height=300)
    #     elif canvas_num == 3:
    #         self.canv3.config(width=300, height=300)
    #     elif canvas_num == 4:
    #         self.canv4.config(width=300, height=300)
    #     else:
    #         print("minimize canvas not working.", canvas_num)
    #         return

    def hideGridElement(self, widget):
        widget.grid_forget()
    
    def showGridElement(self, widget, c=0, r=0):
        widget.grid(coloumn=c, row=r)

    def showSmallDisplay():
        print("showsmall display")

    def displayCamGrid(self):
        self.display_frame_large.grid_forget()
        self.display_frame.grid(column=0, row=0)
    def displayCamZoom(self):
        self.display_frame.grid_forget()
        self.display_frame_large.grid(column=0, row=0, sticky="news")