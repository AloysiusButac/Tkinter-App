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
        
        self.delay = 41             # 24 fps frame delay
        self.vid = MyVideoCapture(0)

        # Main Widow Frames
        self.container_frame = tk.Frame(self.root)
        self.display_frame = tk.Frame(self.container_frame)
        self.display_frame_large = tk.Frame(self.container_frame)
        self.ui_frame = tk.Frame(self.container_frame)

        self.container_frame.columnconfigure(0, weight=2)
        self.container_frame.rowconfigure(0, weight=1)
       

        # Display Frame setup
        self.display_frame.columnconfigure(0, weight=1)
        self.display_frame.columnconfigure(1, weight=1)
        self.display_frame.rowconfigure(0, weight=1)
        self.display_frame.rowconfigure(1, weight=1)

        ## Create Canvas grid
        self.maximized_canvas = [False, False, False, False]
        self.canv1 = tk.Canvas(self.display_frame, bd=0, relief="solid", highlightbackground="#aaa", highlightthickness=2)
        self.canv2 = tk.Canvas(self.display_frame, bd=0, relief="solid", highlightbackground="#aaa", highlightthickness=2)
        self.canv3 = tk.Canvas(self.display_frame, bd=0, relief="solid", highlightbackground="#aaa", highlightthickness=2)
        self.canv4 = tk.Canvas(self.display_frame, bd=0, relief="solid", highlightbackground="#aaa", highlightthickness=2)
        self.canv1.bind("<Button-1>", lambda event: self.displayCamZoom(1))
        self.canv2.bind("<Button-1>", lambda event: self.displayCamZoom(2))
        self.canv3.bind("<Button-1>", lambda event: self.displayCamZoom(3))
        self.canv4.bind("<Button-1>", lambda event: self.displayCamZoom(4))
        self.canv1.grid(column=0, row=0, pady=2, padx=2, stick="news")
        self.canv2.grid(column=1, row=0, pady=2, padx=2, stick="news")
        self.canv3.grid(column=0, row=1, pady=2, padx=2, stick="news")
        self.canv4.grid(column=1, row=1, pady=2, padx=2, stick="news")
        ## Load image on each canvas
        self.img1 = ImageTk.PhotoImage(Image.open("video.png").resize([280, 280], Image.BILINEAR))
        self.img1_large = ImageTk.PhotoImage(Image.open("video.png").resize([560, 560], Image.BILINEAR))
        ## Add image on each canvas
        self.display_frame.update()
        self.canvas1_wh = [self.canv1.winfo_width(), self.canv1.winfo_height()]
        self.canvas2_wh = [self.canv2.winfo_width(), self.canv2.winfo_height()]
        self.canvas3_wh = [self.canv3.winfo_width(), self.canv3.winfo_height()]
        self.canvas4_wh = [self.canv4.winfo_width(), self.canv4.winfo_height()]
        print(self.canvas1_wh[0], self.canvas1_wh[1])
        print(self.canvas2_wh[0], self.canvas2_wh[1])
        print(self.canvas3_wh[0], self.canvas3_wh[1])
        print(self.canvas4_wh[0], self.canvas4_wh[1])

        self.canv1.create_image(0, 0, anchor=tk.CENTER, image=self.img1, tag="c1Stream")
        self.canv2.create_image(0, 0, anchor=tk.CENTER, image=self.img1, tag="c2Stream")
        self.canv3.create_image(0, 0, anchor=tk.CENTER, image=self.img1, tag="c3Stream")
        self.canv4.create_image(0, 0, anchor=tk.CENTER, image=self.img1, tag="c4Stream")

        # Large display setup
        self.canv_big = tk.Canvas(self.display_frame_large, width=650, height=420, bd=0, relief="solid", highlightbackground="#aaa", highlightthickness=2)
        self.canv_big.bind("<Button-1>", lambda event : self.displayCamGrid())
        self.canv_big.pack(padx=10, pady=10, fill="both", expand=True)

        # UI Frame setup
        self.btn1 = tk.Button(self.ui_frame, text="NOTIFICATION", font=self.button_font, bd=1, relief="solid", foreground="#333", command=self.ShowNotification) 
        self.btn2 = tk.Button(self.ui_frame, text="HISTORY", font=self.button_font, bd=1, relief="solid", foreground="#333", command=self.ShowHistory)
        self.btn3 = tk.Button(self.ui_frame, text="MENU", font=self.button_font, bd=1, relief="solid", foreground="#333", command=self.ShowMenu)

        self.btn1.pack(padx=2, pady=2, ipadx=20, side="top", fill=tk.X)
        self.btn2.pack(padx=2, pady=2, ipadx=20, side="top", fill=tk.X)
        self.btn3.pack(padx=2, pady=2, ipadx=20, anchor="e", side="bottom")

        #  Window Frames Deployment
        self.container_frame.pack(padx=10, pady=10, fill="both", expand=True)
        self.display_frame.grid(column=0, row=0, padx=40, pady=20, sticky="nw")
        self.ui_frame.grid(column=1, row=0, padx=10, pady=30, sticky="news")

    def show(self):
        self.update()
        self.root.mainloop()
    
    def update(self):
        ret , frame = self.vid.get_frame()
        if ret:
            self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
            self.canv1.create_image(0, 0, image=self.photo, anchor=tk.NW)
            self.canv2.create_image(0, 0, image=self.photo, anchor=tk.NW)
            self.canv3.create_image(0, 0, image=self.photo, anchor=tk.NW)
            self.canv4.create_image(0, 0, image=self.photo, anchor=tk.NW)
        
        self.root.after(self.delay, self.update)


    def ShowNotification(self):
        print("Notification Clicked!")

    def ShowHistory(self):
        print("History Clicked!")

    def ShowMenu(self):
        print("Menu Clicked!")

    def focusOnCamera(self, event, cam_num=0):
        if cam_num == 1:
            if not self.maximized_canvas[0]:
                self.displayCamGrid()
                self.maximized_canvas[0] = 1
            else:
                self.displayCamZoom()
                self.maximized_canvas[0] = 0
        elif cam_num == 2:
            if not self.maximized_canvas[1]:
                self.displayCamGrid()
                self.maximized_canvas[1] = 1
            else:
                self.displayCamZoom()
                self.maximized_canvas[1] = 0
        elif cam_num == 3:
            if not self.maximized_canvas[2]:
                self.displayCamGrid()
                self.maximized_canvas[2] = 1
            else:
                self.displayCamZoom()
                self.maximized_canvas[2] = 0
        elif cam_num == 4:
            if not self.maximized_canvas[3]:
                self.displayCamGrid()
                self.maximized_canvas[3] = 1
            else:
                self.displayCamZoom()
                self.maximized_canvas[3] = 0
        else:
            print("focus on cam not working.", cam_num)
            return

    def displayCamGrid(self):
        self.display_frame_large.grid_forget()
        self.display_frame.grid(column=0, row=0, padx=40, pady=20, sticky="nw")

    def displayCamZoom(self, cam_index=0):
        self.canv_big.delete("all")
        if cam_index == 1:
            self.canv_big.create_image(0, 0, anchor=tk.NW, image=self.img1_large)
        elif cam_index == 2:
            self.canv_big.create_image(0, 0, anchor=tk.NW, image=self.canv2.itemcget("c2Stream", "image"))
        elif cam_index == 3:
            self.canv_big.create_image(0, 0, anchor=tk.NW, image=self.canv3.itemcget("c3Stream", "image"))
        elif cam_index == 4:
            self.canv_big.create_image(0, 0, anchor=tk.NW, image=self.canv4.itemcget("c4Stream", "image"))
        else:
            print("zoom pass")
            return

        self.display_frame.grid_forget()
        self.display_frame_large.grid(column=0, row=0, padx=20, pady=10, sticky="news")