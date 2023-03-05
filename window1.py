import tkinter as tk
from PIL import Image,ImageTk
from VideoCapture import *
from tkinter import Toplevel
from NotificationWindow import *
from HistoryWindow import *
import cv2

class Window1:
    button_font = ("Arial", 14)

    def __init__(self, parent, title = "Window 1", width = 1100, height = 600):
        self.root = parent
        window_w = width
        window_h = height
        if isinstance(parent, tk.Tk):
            self.pos_x = (self.root.winfo_screenwidth() // 2) - (window_w // 2)
            self.pos_y = (self.root.winfo_screenheight() // 2) - (window_h // 2) - 50
            self.root.geometry('{}x{}+{}+{}'.format(window_w, window_h, self.pos_x, self.pos_y))
            self.root.title(title)
            self.root.resizable(0, 0)
        
        self.active_stream = 1
        self.delay = 41             # 24 fps frame delay
        self.vid_large = MyVideoCapture(0) 
        self.set_record = False

        # Main Window Frames
        self.container_frame = tk.Frame(self.root, bg="#9bb")
        self.container_frame.columnconfigure(0, weight=10, minsize=(width-100)*0.8//1)
        self.container_frame.columnconfigure(1, weight=1, minsize=(width-100)*0.2//1)
        self.container_frame.rowconfigure(0, weight=1, minsize=height-50)
        self.display_frame_cover = tk.Frame(self.container_frame, bg="#9bb") # COVER
        self.display_frame = tk.Frame(self.display_frame_cover, bg="#9bb")
        self.display_frame_large = tk.Frame(self.display_frame_cover, bg="#9bb")
        self.ui_frame_cover = tk.Frame(self.container_frame, bg="#345") # COVER
        self.ui_frame = tk.Frame(self.ui_frame_cover, bg="#345")
        self.notification_frame = NotificationWindow(self.display_frame_cover).get_window()
        self.history_frame = HistoryWindow(self.display_frame_cover).get_window()

        # Menu Window setup
        self.MenuWindow = Toplevel(self.root)
        self.MenuWindow.geometry("{}x{}+{}+{}".format(300, 300, 300, 300))
        self.MenuWindow.title("Menu window")
        self.MenuWindow.withdraw()
        self.menu_btn = tk.Button(self.MenuWindow, text='Window2')
        self.menu_btn.pack(padx=10, pady=10)

        # Display Frame setup
        self.display_frame.columnconfigure(0, weight=1)
        self.display_frame.columnconfigure(1, weight=1)
        self.display_frame.rowconfigure(0, weight=1)
        self.display_frame.rowconfigure(1, weight=1)

        ## Create Canvas grid
        self.canv1 = tk.Canvas(self.display_frame, bd=0, bg="black", relief="solid", highlightbackground="#aaa", highlightthickness=2)
        self.canv2 = tk.Canvas(self.display_frame, bd=0, bg="black", relief="solid", highlightbackground="#aaa", highlightthickness=2)
        self.canv3 = tk.Canvas(self.display_frame, bd=0, bg="black", relief="solid", highlightbackground="#aaa", highlightthickness=2)
        self.canv4 = tk.Canvas(self.display_frame, bd=0, bg="black", relief="solid", highlightbackground="#aaa", highlightthickness=2)
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

        # Large display setup
        self.canv_big = tk.Canvas(self.display_frame_large, bd=0, relief="solid", highlightbackground="#aaa", highlightthickness=2)
        self.canv_big.bind("<Button-1>", lambda event : self.displayCamGrid())
        self.canv_big.pack(padx=10, pady=10, fill="both", expand=True)

        # UI Frame setup
        self.btn1 = tk.Button(self.ui_frame, text="NOTIFICATION", font=self.button_font, bd=1, relief="solid", foreground="#333", command=self.ShowNotification) 
        self.btn2 = tk.Button(self.ui_frame, text="HISTORY", font=self.button_font, bd=1, relief="solid", foreground="#333", command=self.ShowHistory)
        self.btn3 = tk.Button(self.ui_frame, text="MENU", font=self.button_font, bd=1, relief="solid", foreground="#333", command=self.ShowMenu)

        self.btn1.pack(padx=2, pady=2, ipadx=20, anchor="n", side="top", fill="x")
        self.btn2.pack(padx=2, pady=2, ipadx=20, anchor="n", side="top", fill="x")
        self.btn3.pack(padx=2, pady=2, ipadx=20, anchor="e", side="bottom")

        #  Window Frames Deployment
        self.container_frame.pack(padx=0, pady=0, fill="both", expand=True)
        self.display_frame.pack(padx=10, pady=10, fill="both", expand=True)
        self.display_frame_cover.grid(column=0, row=0, padx=10, pady=20, sticky="nw")
        self.ui_frame.pack(padx=20, pady=10, fill="both", expand=True)
        self.ui_frame_cover.grid(column=1, row=0, padx=0, pady=0, ipadx=10, ipady=0, sticky="news")

        self.display_frame.update()
        self.display_frame_large.update_idletasks()
        self.canvas1_wh = [self.canv1.winfo_width(), self.canv1.winfo_height()]
        self.canvas2_wh = [self.canv2.winfo_width(), self.canv2.winfo_height()]
        self.canvas3_wh = [self.canv3.winfo_width(), self.canv3.winfo_height()]
        self.canvas4_wh = [self.canv4.winfo_width(), self.canv4.winfo_height()]
        self.canvasbig_wh = [self.canv_big.winfo_width(), self.canv_big.winfo_height()] 

    def show(self):
        self.update()
        # self.root.mainloop()
    
    def update(self):
        if(self.vid1.grab_frame() and self.vid2.grab_frame() and self.vid3.grab_frame() and self.vid4.grab_frame()):
            ret1, frame1 = self.vid1.retrieve_frame()
            ret2, frame2 = self.vid2.retrieve_frame()
            ret3, frame3 = self.vid3.retrieve_frame()
            ret4, frame4 = self.vid4.retrieve_frame()
            self.display_frame.update()
            if ret1:
                self.photo1 = ImageTk.PhotoImage(image=Image.fromarray(frame1).resize((self.canvas1_wh[0], self.canvas1_wh[1]), Image.BILINEAR))
                self.canv1.create_image(self.canvas1_wh[0]//2, self.canvas1_wh[1]//2, image=self.photo1, anchor=tk.CENTER)
                self.canv1.create_text(40, self.canvas1_wh[1]-10, text="Cam 1", fill="white", font=("Arial 15 bold"))
                if self.set_record:
                    self.RecordStream(self.vid1)
            if ret2:
                self.photo2 = ImageTk.PhotoImage(image=Image.fromarray(frame2).resize((self.canvas2_wh[0], self.canvas2_wh[1]), Image.BILINEAR))
                self.canv2.create_image(self.canvas2_wh[0]//2, self.canvas2_wh[1]//2, image=self.photo2, anchor=tk.CENTER)
                self.canv2.create_text(40, self.canvas2_wh[1]-10, text="Cam 2", fill="white", font=("Arial 15 bold"))
                if self.set_record:
                    self.RecordStream(self.vid2)
            if ret3:
                self.photo3 = ImageTk.PhotoImage(image=Image.fromarray(frame3).resize((self.canvas3_wh[0], self.canvas3_wh[1]), Image.BILINEAR))
                self.canv3.create_image(self.canvas3_wh[0]//2, self.canvas3_wh[1]//2, image=self.photo3, anchor=tk.CENTER)
                self.canv3.create_text(40, self.canvas3_wh[1]-10, text="Cam 3", fill="white", font=("Arial 15 bold"))
                if self.set_record:
                    self.RecordStream(self.vid3)
            if ret4:
                self.photo4 = ImageTk.PhotoImage(image=Image.fromarray(frame4).resize((self.canvas4_wh[0], self.canvas4_wh[1]), Image.BILINEAR))
                self.canv4.create_image(self.canvas4_wh[0]//2, self.canvas4_wh[1]//2, image=self.photo4, anchor=tk.CENTER)
                self.canv4.create_text(40, self.canvas4_wh[1]-10, text="Cam 4", fill="white", font=("Arial 15 bold"))
                if self.set_record:
                    self.RecordStream(self.vid4)
            
            if self.display_frame_large.winfo_ismapped():
                enlarged_frame_id = 1
                retl, framel = self.vid1.retrieve_frame()
                if self.active_stream == 2:
                    retl, framel = self.vid2.retrieve_frame()
                    enlarged_frame_id = 2
                elif self.active_stream == 3:
                    retl, framel = self.vid3.retrieve_frame()
                    enlarged_frame_id = 3
                elif self.active_stream == 4:
                    retl, framel = self.vid4.retrieve_frame()
                    enlarged_frame_id = 4

                if retl:
                    height, width, channels = framel.shape
                    self.photo_large = ImageTk.PhotoImage(image=Image.fromarray(framel).resize(self.ScaleDimensions((width, height)), Image.BILINEAR))
                    self.canv_big.create_image(self.canv_big.winfo_width()//2, self.canv_big.winfo_width()//2-150, image=self.photo_large, anchor=tk.CENTER)
                    self.canv_big.create_text(100, self.canv_big.winfo_height()-20, text="CAMERA {}".format(enlarged_frame_id), fill="white", font=("Arial 20 bold"))
        else:
            pass
        
        self.root.after(self.delay, self.update)

    def SetStream1(self, stream):
        self.vid1 = stream

    def SetStream2(self, stream):
        self.vid2 = stream

    def SetStream3(self, stream):
        self.vid3 = stream

    def SetStream4(self, stream):
        self.vid4 = stream

    def RecordStream(self, stream):
        stream.write_frame()

    def ShowNotification(self):
        print("Notification Clicked!")

        self.display_frame_cover.update()

        # if self.display_frame.winfo_manager():
        #     self.display_frame.grid_forget()
        # elif self.display_frame_large.winfo_manager():
        #     self.display_frame_large.grid_forget()
        # elif self.history_frame.winfo_manager():
        #     self.history_frame.grid_forget()

        # if not self.notification_frame.winfo_manager():
        #     self.notification_frame.grid(column=0, row=0, padx=10, pady=10, sticky="news")
        # else:
        #     self.notification_frame.grid_forget()
        #     self.display_frame_large.grid_forget()
        #     self.display_frame.grid(column=0, row=0, padx=40, pady=20, sticky="nw")
        if self.display_frame.winfo_manager():
            self.display_frame.pack_forget()
        elif self.display_frame_large.winfo_manager():
            self.display_frame_large.pack_forget()
        elif self.history_frame.winfo_manager():
            self.history_frame.pack_forget()

        if not self.notification_frame.winfo_manager():
            self.notification_frame.pack(padx=10, pady=10, fill="both", expand=True)
        else:
            self.notification_frame.pack_forget()
            self.display_frame_large.pack_forget()
            self.display_frame.pack(padx=40, pady=20, fill="both", expand=True)


    def ShowHistory(self):
        print("History Clicked!")

        self.display_frame_cover.update()

        if self.display_frame.winfo_manager():
            self.display_frame.pack_forget()
        elif self.display_frame_large.winfo_manager():
            self.display_frame_large.pack_forget()
        elif self.notification_frame.winfo_manager():
            self.notification_frame.pack_forget()

        if not self.history_frame.winfo_manager():
            self.history_frame.pack(padx=10, pady=10, fill="both", expand=True)
        else:
            self.history_frame.pack_forget()
            self.display_frame_large.pack_forget()
            self.display_frame.pack(padx=40, pady=20, fill="Both", expand=True)

    def ShowMenu(self):
        print("Menu Clicked!")

        self.MenuWindow.deiconify()

        tmp = tk.Label(self.MenuWindow, text="Menu shows up here.")
        tmp.pack(padx=20, pady=20)

        # self.menu_btn = tk.Button(self.MenuWindow, text='Window 2')
        # self.menu_btn.pack(padx=10, pady=10)
    
    def setMenuButtonCommand(self, command):
        self.MenuWindow.update()
        if self.menu_btn is not None:
            self.menu_btn.configure(command=command)

    def displayCamGrid(self):
        # self.display_frame_large.grid_forget()
        # self.display_frame.grid(column=0, row=0, padx=10, pady=20, sticky="news")
        self.display_frame_large.pack_forget()
        self.display_frame.pack(padx=10, pady=20, fill="both", expand=True)

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

        self.display_frame.pack_forget()
        self.display_frame_large.pack(padx=10, pady=20, fill="both", expand=True)

    def CreateNotificationPill(self, parent, imgpath="", title="title", message="Notification message", width=500, height=100, font=None, side="top"):
        container = tk.Frame(parent, bd=2)
        # lbl_title = tk.Label(container, text=title)
        lbl_message = tk.Label(container, text="{}: {}".format(title, message))
        # canv = tk.Canvas(container, height=40, width=40, bd=0, highlightbackground="#222", highlightthickness=2)
        
        # lbl_title.pack(padx=20, pady=0, side=side)
        lbl_message.pack(padx=20, pady=0, side=side)
        # canv.pack(padx=2, pady=2, side="left")

        return container

    def CreateHistoryPill(self, parent, imgpath="", title="title", width=500, height=100, font=None, side="top"):
        container = tk.Frame(parent, bd=2)
        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=10)
        container.rowconfigure(0, weight=1)
        lbl_message = tk.Label(container, text="{}".format(title))
        canv = tk.Canvas(container, height=40, width=40, bd=0, highlightbackground="#222", highlightthickness=2)
        
        lbl_message.grid(padx=20, column=1, row=0, sticky="news")
        canv.grid(padx=10, column=0, row=0, sticky="news")

        return container

    def ScaleDimensions(self, dim1=(338, 266), dim2=(704, 540)):
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
