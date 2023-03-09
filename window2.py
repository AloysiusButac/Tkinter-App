import tkinter as tk
from tkinter.ttk import Separator, Style
from PIL import ImageTk, Image
from Util import *

# https://www.activestate.com/resources/quick-reads/how-to-add-images-in-tkinter/
# https://www.c-sharpcorner.com/blogs/basics-for-displaying-image-in-tkinter-python

class Window2(tk.Frame):

    font = ("Arial", 12)
    button_font = ("Arial", 13)

    def __init__(self, parent, title = "Window 2", width = 1200, height = 600):
        super().__init__(parent)

        self.root = tk.Frame(parent)
        window_w = width
        window_h = height
        if isinstance(parent, tk.Tk):
            pos_x = (parent.winfo_screenwidth() // 2) - (window_w // 2)
            pos_y = (parent.winfo_screenheight() // 2) - (window_h // 2) - 50
            # self.root.geometry('{}x{}+{}+{}'.format(window_w, window_h, pos_x, pos_y))
            # self.root.title(title)
            # self.root.resizable(0, 0)

        self.root.columnconfigure(0, weight=2, minsize=240)
        self.root.columnconfigure(1, weight=6)
        self.root.columnconfigure(2, weight=6)
        self.root.rowconfigure(0, weight=1)

        """
              Sidebar
            --=========------------------------------
            ||    1    |                            !
            ||_________|                            !
            ||         |                            !
            ||    2    |                            !
            ||_________|                            !
            ||         |                            !
            ||    3    |                            !
            ||         |                            !
            ||=========|----------------------------!
        """

        # Sidebar 
        sidebar_frame = tk.Frame(self.root, bg="#fff")
        sidebar_frame.rowconfigure(0, weight=1)
        sidebar_frame.rowconfigure(1, weight=3)
        sidebar_frame.rowconfigure(2, weight=1)
        sidebar_frame.rowconfigure(3, weight=2)
        # Image & Buttons
        img = tk.Canvas(sidebar_frame, bd=1, bg="#fff", relief="solid", height=200, width=230)
        # img = tk.Canvas(sidebar_frame, height=200, width=230)
        self.sidebar_image = ImageTk.PhotoImage(Image.open("video.png").resize([200, 200], Image.BILINEAR))
        img.create_image(115, 100, anchor=tk.CENTER, image=self.sidebar_image)
        # btn_container = tk.Frame(sidebar_frame, bg="#aaa", bd=1, relief="solid")
        btn_container = tk.Frame(sidebar_frame, bg="#fff")
        side_btns = self.CreateButtonArray(btn_container, 3, ["Button"] * 3, anchor="top")
        for b in side_btns:
            b.pack(ipady=10, padx=5, pady=0, fill="x", expand=True)

        # Connection Status panel
        # connection_status_frame = tk.Frame(sidebar_frame, bg="#bbb", bd=1, relief="solid")
        connection_status_frame = tk.Frame(sidebar_frame, bg="#fff")
        connection_status_frame.rowconfigure(0, weight=1)
        connection_status_frame.rowconfigure(1, weight=1)
        connection_status_frame.rowconfigure(2, weight=1)
        connection_status_frame.columnconfigure(0, weight=1)

        sp = Separator(sidebar_frame, orient="horizontal")
        sp.grid(column=0, row=2, sticky="we")
        style = Style(self.root)
        style.configure("TSeparator", bg="#222", relief="solid")
        ## Connection Status Elements
        lbl_connstat = tk.Label(connection_status_frame, text="Connection Status:", font=self.font, bg="#fff")
        srv_frme = tk.Frame(connection_status_frame, bg="#fff")
        srv_frme.columnconfigure(0, weight=1)
        srv_frme.rowconfigure(0, weight=1)
        srv_frme.rowconfigure(1, weight=1)
        lbl_svr = tk.Label(srv_frme, text="Server:", font=self.font, bg="#fff")
        btn_srv = tk.Button(srv_frme, text="Button", font=self.button_font, bd=1, bg="#fff", relief="solid", foreground="#333")
        alrt_frme = tk.Frame(connection_status_frame, bg="#fff")
        alrt_frme.columnconfigure(0, weight=1)
        alrt_frme.rowconfigure(0, weight=1)
        alrt_frme.rowconfigure(1, weight=1)
        lbl_alrt = tk.Label(alrt_frme, text="Alert Module:", font=self.font, bg="#fff")
        btn_alrt = tk.Button(alrt_frme, text="Button", font=self.button_font, bd=1, bg="#fff", relief="solid", foreground="#333")
        lbl_connstat.pack(padx=10, pady=0, fill="x")
        lbl_svr.grid(column=0, row=0, sticky="nw")
        btn_srv.grid(ipadx=20, ipady=5, padx=5, pady=0, column=0, row=1, sticky="ew")
        lbl_alrt.grid(column=0, row=0, sticky="nw")
        btn_alrt.grid(ipadx=20, ipady=5, padx=5, pady=0, column=0, row=1, sticky="ew")
        srv_frme.pack(padx=5, pady=5, fill="both", expand=True)
        alrt_frme.pack(padx=5, pady=5, fill="both", expand=True)
        ## Positioning Elements in grid within frame
        img.grid(column=0, row=0, padx=0, pady=0, sticky="news")
        btn_container.grid(column=0, row=1, padx=5, pady=10, sticky="new")
        connection_status_frame.grid(column=0, row=3, padx=10, pady=0, sticky="news")

        """
                                 Main Panel 
            -----------==============================-
            !          |______________1_____________||
            !          |                            ||
            !          |______________2_____________||
            !          |                            ||
            !          |                            ||
            !          |              3             ||
            !          |                            ||
            !          |                            ||
            !----------|============================||
        """
        # Main Panel
        # data_frame = tk.Frame(self.root, bd=1, relief="solid", bg="#7af")
        data_frame = tk.Frame(self.root, bd=1, relief="solid", bg="#fff")

        data_frame.rowconfigure(0, weight=1)
        data_frame.rowconfigure(1, weight=1)
        data_frame.rowconfigure(2, weight=4, minsize=60)
        data_frame.rowconfigure(3, weight=1)
        data_frame.rowconfigure(4, weight=15)
        data_frame.columnconfigure(0, weight=1)

        # data_frame_menu = tk.Frame(data_frame, bg="yellow", bd=1, relief="solid")
        # data_frame_ribbon = tk.Frame(data_frame, bg="yellow", bd=1, relief="solid")
        # data_frame_canvases = tk.Frame(data_frame, bg="yellow", bd=1, relief="solid")
        data_frame_menu = tk.Frame(data_frame, bg="#fff")
        data_frame_ribbon = tk.Frame(data_frame, bg="#fff")
        data_frame_canvases = tk.Frame(data_frame, bg="#fff")

        # Menu frame Elements
        btn_home = tk.Button(data_frame_menu, text="Home", font=self.button_font, bg="#fff", bd=0).pack(side="left", ipadx=10)
        
        # Ribbon frame Elements
        data_frame_ribbon.rowconfigure(0, weight=1)
        data_frame_ribbon.columnconfigure(0, weight=1)

        # rbnfrme_stat = tk.Frame(data_frame_ribbon, bd=0, highlightbackground="#222", highlightthickness=2)
        rbnfrme_stat = tk.Frame(data_frame_ribbon, bg="#fff")

        self.default_image = ImageTk.PhotoImage(Image.open("video.png").resize([50, 50], Image.BILINEAR))

        rbncanv_1 = self.CreateStatPill(rbnfrme_stat, self.default_image, title="Anomally Detecter")
        rbncanv_2 = self.CreateStatPill(rbnfrme_stat, self.default_image, title="Audio Detected")
        rbncanv_3 = self.CreateStatPill(rbnfrme_stat, self.default_image, title="Total Detection")

        rbncanv_1.pack(padx=10, pady=0, fill="x", expand=True, side="left")
        rbncanv_2.pack(padx=10, pady=0, fill="x", expand=True, side="left")
        rbncanv_3.pack(padx=10, pady=0, fill="x", expand=True, side="left")

        rbnfrme_stat.grid(padx=100, column=0, row=0, sticky="news")

        # Data frame Elements
        data_frame_canvases.rowconfigure(0, weight=10)
        data_frame_canvases.rowconfigure(1, weight=1)
        data_frame_canvases.columnconfigure(0, weight=1)
        data_frame_canvases.columnconfigure(1, weight=3)
        data_frame_canvases_recent = tk.Frame(data_frame_canvases, bg="#fff")
        data_frame_canvases_detected = tk.Frame(data_frame_canvases, bg="#fff")

        self.pill_img1 = ImageTk.PhotoImage(Image.open("graph.png").resize([400, 100], Image.BILINEAR))
        self.pill_img2 = ImageTk.PhotoImage(Image.open("graph2.png").resize([140, 280], Image.BILINEAR))

        data_canv1 = self.CreateDataPill(data_frame_canvases_detected, self.pill_img1, "Anomaly Detected")
        data_canv2 = self.CreateDataPill(data_frame_canvases_detected, self.pill_img1, "Audio Detected")

        data_canv3 = self.CreateDataPill(data_frame_canvases_recent, self.pill_img2, "Recent Anomaly\nDetected", side="top", width=170, height=350)
        data_canv4 = self.CreateDataPill(data_frame_canvases_recent, self.pill_img2, "Recent Audio\nDetected", side="top", width=170, height=350)

        data_canv1.pack(padx=20, pady=10, side="top")
        data_canv2.pack(padx=20, pady=10, side="top")
        data_canv3.pack(padx=5, pady=0, side="left")
        data_canv4.pack(padx=5, pady=0, side="left")
        data_frame_canvases_detected.grid(column=0, row=0, sticky="news")
        data_frame_canvases_recent.grid(column=1, row=0, padx=10, pady=0, sticky="news")

        data_frame_canvases_buttons = tk.Frame(data_frame_canvases, bg="#fff")
        data_buttons = self.CreateButtonArray(data_frame_canvases_buttons, 3, ["Button"]*3)
        for btn in data_buttons:
            btn.pack(padx=5, pady=5, ipadx=15, ipady=0, side="left")
        data_frame_canvases_buttons.grid(column=0, row=1, padx=10, pady=0, sticky="news")
        
        data_button_far_right = self.CreateButtonArray(data_frame_canvases, 1, ["Button"], anchor="right")
        data_button_far_right[0].grid(column=1, row=1, padx=10, pady=0, ipadx=15, ipady=0, sticky="e")

        # Data frame internal frame positioning
        sp_menu = Separator(data_frame, orient="horizontal")
        sp_menu.grid(column=0, row=1, sticky="we")
        sp_ribbon = Separator(data_frame, orient="horizontal") 
        sp_ribbon.grid(column=0, row=3, sticky="we")
        data_frame_menu.grid(column=0, row=0, padx=0, pady=0, sticky="new")
        data_frame_ribbon.grid(column=0, row=2, padx=0, pady=0, sticky="nsew")
        data_frame_canvases.grid(column=0, row=4, padx=0, pady=0, sticky="news")

        # Positioning frames within window
        sidebar_frame.grid(column=0, row=0, columnspan=1, rowspan=1, padx=0, pady=0, sticky="news")
        data_frame.grid(column=1, row=0, columnspan=2, rowspan=1, padx=0, pady=0, sticky="news")
    
    def show(self):
        self.root.mainloop()

    def closeWindow(self):
        self.root.close()