import tkinter as tk
from PIL import Image,ImageTk
from VideoCapture import *
import cv2

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
        
        self.active_stream = 1
        self.delay = 41             # 24 fps frame delay
        self.vid1 = MyVideoCapture(0)
        self.vid2 = MyVideoCapture("sample.mkv")
        self.vid3 = MyVideoCapture("3.gif")
        self.vid4 = MyVideoCapture("4.gif")
        self.vid_large = MyVideoCapture("sample.mkv") 

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
        # self.canv1.create_image(0, 0, anchor=tk.CENTER, image=self.img1, tag="c1Stream")
        # self.canv2.create_image(0, 0, anchor=tk.CENTER, image=self.img1, tag="c2Stream")
        # self.canv3.create_image(0, 0, anchor=tk.CENTER, image=self.img1, tag="c3Stream")
        # self.canv4.create_image(0, 0, anchor=tk.CENTER, image=self.img1, tag="c4Stream")

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

        self.display_frame.update()
        self.display_frame_large.update_idletasks()
        self.canvas1_wh = [self.canv1.winfo_width(), self.canv1.winfo_height()]
        self.canvas2_wh = [self.canv2.winfo_width(), self.canv2.winfo_height()]
        self.canvas3_wh = [self.canv3.winfo_width(), self.canv3.winfo_height()]
        self.canvas4_wh = [self.canv4.winfo_width(), self.canv4.winfo_height()]
        self.canvasbig_wh = [self.canv_big.winfo_width(), self.canv_big.winfo_height()] 
        print(self.canvas1_wh[0], self.canvas1_wh[1])
        print(self.canvas2_wh[0], self.canvas2_wh[1])
        print(self.canvas3_wh[0], self.canvas3_wh[1])
        print(self.canvas4_wh[0], self.canvas4_wh[1])
        print(self.canvasbig_wh[0], self.canvasbig_wh[1])

    def show(self):
        self.update()
        self.root.mainloop()
    
    def rescale_frame(frame, percent=75):
        width = int(frame.shape[1] * percent/ 100)
        height = int(frame.shape[0] * percent/ 100)
        dim = (width, height)
        return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

    def frame_scaler(self, index=1, percent=100):
        height, width = 0
        if index == 1:
            width = self.vid1.get(3)
            height = self.vid1.get(4)
        elif index == 2:
            width = self.vid2.get(3)
            height = self.vid2.get(4)
        elif index == 3:
            width = self.vid3.get(3)
            height = self.vid3.get(4)
        elif index == 4:
            width = self.vid4.get(3)
            height = self.vid4.get(4)
        else:
            print("Frame scaler error.")
            return
        
        return (width * percent / 100, height * percent / 100)
    
    def update(self):
        ret1 , frame1 = self.vid1.get_frame()
        ret2, frame2 = self.vid2.get_frame()
        ret3, frame3 = self.vid3.get_frame()
        ret4, frame4 = self.vid4.get_frame()
        if ret1:
            self.photo1 = ImageTk.PhotoImage(image=Image.fromarray(frame1).resize((self.canvas1_wh[0], self.canvas1_wh[1]), Image.BILINEAR))
            self.canv1.create_image(self.canvas1_wh[0]//2, self.canvas1_wh[1]//2, image=self.photo1, anchor=tk.CENTER)
        if ret2:
            self.photo2 = ImageTk.PhotoImage(image=Image.fromarray(frame2).resize((self.canvas2_wh[0], self.canvas2_wh[1]), Image.BILINEAR))
            self.canv2.create_image(self.canvas2_wh[0]//2, self.canvas2_wh[1]//2, image=self.photo2, anchor=tk.CENTER)
        if ret3:
            self.photo3 = ImageTk.PhotoImage(image=Image.fromarray(frame3).resize((self.canvas3_wh[0], self.canvas3_wh[1]), Image.BILINEAR))
            self.canv3.create_image(self.canvas3_wh[0]//2, self.canvas3_wh[1]//2, image=self.photo3, anchor=tk.CENTER)
        if ret4:
            self.photo4 = ImageTk.PhotoImage(image=Image.fromarray(frame4).resize((self.canvas4_wh[0], self.canvas4_wh[1]), Image.BILINEAR))
            self.canv4.create_image(self.canvas4_wh[0]//2, self.canvas4_wh[1]//2, image=self.photo4, anchor=tk.CENTER)
        
        if self.display_frame_large.winfo_ismapped():
            retl, framel = self.vid1.get_frame()
            if self.active_stream == 2:
                retl, framel = self.vid2.get_frame()
            elif self.active_stream == 3:
                retl, framel = self.vid3.get_frame()
            elif self.active_stream == 4:
                retl, framel = self.vid4.get_frame()

            if retl:
                height, width, channels = framel.shape
                self.photo_large = ImageTk.PhotoImage(image=Image.fromarray(framel).resize(self.ScaleDimensions((width, height)), Image.BILINEAR))
                self.canv_big.create_image(self.canv_big.winfo_width()//2, self.canv_big.winfo_width()//2-80, image=self.photo_large, anchor=tk.CENTER)
        else:
            pass
        
        self.root.after(self.delay, self.update)


    def ShowNotification(self):
        print("Notification Clicked!")

    def ShowHistory(self):
        print("History Clicked!")

    def ShowMenu(self):
        print("Menu Clicked!")

    def ScaleDimensions(self, dim1=(338, 266), dim2=(704, 540)):
        m = dim2[0] / dim1[0]
        n = dim2[1] / dim1[1]
        if (m < n):
            return (int(dim1[0] * m), int(dim1[1] * m))
        else:
            return (int(dim1[0] * n), int(dim1[1] * n))

    def displayCamGrid(self):
        self.display_frame_large.grid_forget()
        self.display_frame.grid(column=0, row=0, padx=40, pady=20, sticky="nw")

    def displayCamZoom(self, cam_index=0):
        self.canv_big.delete("all")
        if cam_index == 1:
            self.active_stream = 1
        elif cam_index == 2:
            self.active_stream = 2
        elif cam_index == 3:
            self.active_stream = 3
        elif cam_index == 4:
            self.active_stream = 4
        else:
            print("zoom pass")
            self.active_stream = 1
            return

        self.display_frame.grid_forget()
        self.display_frame_large.grid(column=0, row=0, padx=20, pady=10, sticky="news")