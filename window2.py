import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

# https://www.activestate.com/resources/quick-reads/how-to-add-images-in-tkinter/
# https://www.c-sharpcorner.com/blogs/basics-for-displaying-image-in-tkinter-python

class Window2():
    def __init__(self, parent, title = "Window 2", width = 1000, height = 600):
        self.root = parent
        window_w = width
        window_h = height
        if isinstance(parent, tk.Tk):
            pos_x = (self.root.winfo_screenwidth() // 2) - (window_w // 2)
            pos_y = (self.root.winfo_screenheight() // 2) - (window_h // 2) - 50
            self.root.geometry('{}x{}+{}+{}'.format(window_w, window_h, pos_x, pos_y))
            self.root.title(title)
            self.root.resizable(0, 0)

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=6)
        self.root.columnconfigure(2, weight=6)
        self.root.rowconfigure(0, weight=1)

        # Menubar
        # menu = tk.Menu(self.root)
        # self.root.config(menu=menu)
        # fileMenu = tk.Menu(menu)
        # fileMenu.add_command(label="Item")
        # fileMenu.add_command(label="Exit")
        # menu.add_cascade(label="File", menu=fileMenu)
        # editMenu = tk.Menu(menu)
        # editMenu.add_command(label="Undo")
        # editMenu.add_command(label="Redo")
        # menu.add_cascade(label="Edit", menu=editMenu)

        """
              Sidebar
            --=========------------------------------
            || / / / / |                            !
            ||/ / / / /|                            !
            || / / / / |                            !
            ||/ / / / /|                            !
            || / / / / |                            !
            ||/ / / / /|                            !
            || / / / / |                            !
            ||/ / / / /|                            !
            ||=========|----------------------------!
        """

        # Sidebar 
        sidebar_frame = tk.Frame(self.root)
        sidebar_frame.rowconfigure(0, weight=1)
        sidebar_frame.rowconfigure(1, weight=3)
        sidebar_frame.rowconfigure(2, weight=2)
        ## Image & Buttons
        img = tk.Canvas(sidebar_frame, bg="#999", bd=1, relief="solid", height=60, width=175)
        btn_container = tk.Frame(sidebar_frame, bg="#aaa", bd=1, relief="solid")
        btn1 = tk.Button(btn_container, text="Button").pack(padx=1, pady=2, fill="both")
        btn2 = tk.Button(btn_container, text="Button").pack(padx=1, pady=2, fill="both")
        btn3 = tk.Button(btn_container, text="Button").pack(padx=1, pady=2, fill="both")
        btn4 = tk.Button(btn_container, text="Button").pack(padx=1, pady=2, fill="both")
        # Connection Status panel
        connection_status_frame = tk.Frame(sidebar_frame, bg="#bbb", bd=1, relief="solid")
        connection_status_frame.rowconfigure(0, weight=1)
        connection_status_frame.rowconfigure(1, weight=1)
        connection_status_frame.rowconfigure(2, weight=1)
        connection_status_frame.columnconfigure(0, weight=1)
        connection_status_frame.columnconfigure(1, weight=1)
        connection_status_frame.columnconfigure(2, weight=1)
        ## Connection Status Elements
        lbl_connstat = tk.Label(connection_status_frame, text="Connection Status:")
        btn_cn1 = tk.Button(connection_status_frame, text="Button")
        btn_cn2 = tk.Button(connection_status_frame, text="Button")
        btn_cn3 = tk.Button(connection_status_frame, text="Button")
        ## Positioning Elements in grid within frame
        img.grid(column=0, row=0, padx=0, pady=0, sticky="news")
        btn_container.grid(column=0, row=1, padx=0, pady=0, sticky="new")
        lbl_connstat.grid(column=0, row=0, padx=0, pady=0, columnspan=3)
        btn_cn1.grid(column=0, row=1, padx=2, pady=0, columnspan=3, sticky="new")
        btn_cn2.grid(column=0, row=2, padx=2, pady=0, columnspan=2, sticky="new")
        btn_cn3.grid(column=2, row=2, padx=2, pady=0, columnspan=1, sticky="new")
        connection_status_frame.grid(column=0, row=2, padx=10, pady=0, sticky="news")

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
        data_frame = tk.Frame(self.root, bd=1, relief="solid", bg="#7af")

        data_frame.rowconfigure(0, weight=1)
        data_frame.rowconfigure(1, weight=4, minsize=60)
        data_frame.rowconfigure(2, weight=15)
        data_frame.columnconfigure(0, weight=1)

        data_frame_menu = tk.Frame(data_frame, bg="yellow", bd=1, relief="solid")
        data_frame_ribbon = tk.Frame(data_frame, bg="yellow", bd=1, relief="solid")
        data_frame_canvases = tk.Frame(data_frame, bg="yellow", bd=1, relief="solid")

        lbl_menu = tk.Label(data_frame_menu, text="menu").pack(fill="both")
        # lbl_ribb = tk.Label(data_frame_ribbon, text="ribbon").pack(fill="both")
        # lbl_canv = tk.Label(data_frame_canvases, text="data").pack(fill="both")

        # data_frame_menu.pack(fill="both", expand=True)
        # data_frame_ribbon.pack(fill="both", expand=True)
        # data_frame_canvases.pack(fill="both", expand=True)

        # Menu frame Elements
        btn_home = tk.Button(data_frame_menu, text="Home", relief="flat").pack(side="left", ipadx=10)
        
        # Ribbon frame Elements
        data_frame_ribbon.rowconfigure(0, weight=1)
        data_frame_ribbon.rowconfigure(1, weight=1)
        data_frame_ribbon.columnconfigure(0, weight=3)
        data_frame_ribbon.columnconfigure(1, weight=5)

        rbnfrme_date = tk.Frame(data_frame_ribbon, bd=0, bg="green", highlightbackground="#222", highlightthickness=2)
        rbnfrme_btn = tk.Frame(data_frame_ribbon, bd=0, highlightbackground="#222", highlightthickness=2)
        rbnfrme_stat = tk.Frame(data_frame_ribbon, bd=0, highlightbackground="#222", highlightthickness=2)

        rbnlbl_sdate = tk.Label(rbnfrme_date, text="Start Date")
        rbnlbl_edate = tk.Label(rbnfrme_date, text="End Date")
        # rbnbtn_1 = tk.Button(rbnfrme_btn, text="Button")
        # rbnbtn_2 = tk.Button(rbnfrme_btn, text="Button")
        # rbnbtn_3 = tk.Button(rbnfrme_btn, text="Button")
        # rbnbtn_4 = tk.Button(rbnfrme_btn, text="Button")
        # rbnbtn_5 = tk.Button(rbnfrme_btn, text="Button")
        # rbnbtn_6 = tk.Button(rbnfrme_btn, text="Button", command=self.root.destroy)
        listbtnnames = ["Button x"] * 6
        rbnbtns = self.CreateButtonArray(rbnfrme_btn, count=6, titles=listbtnnames)
        rbncanv_1 = self.CreateStatPill(rbnfrme_stat, title="Shit works")
        rbncanv_2 = self.CreateStatPill(rbnfrme_stat, title="Shit works")
        rbncanv_3 = self.CreateStatPill(rbnfrme_stat, title="Shit works")

        rbnlbl_sdate.pack(ipadx=15, ipady=5, padx=10, pady=10, side="left")
        rbnlbl_edate.pack(ipadx=15, ipady=5, padx=10, pady=10, side="left")
        # rbnbtn_1.pack(ipadx=10, ipady=0, padx=2, pady=10, side="left")
        # rbnbtn_2.pack(ipadx=10, ipady=0, padx=2, pady=10, side="left")
        # rbnbtn_3.pack(ipadx=10, ipady=0, padx=2, pady=10, side="left")
        # rbnbtn_4.pack(ipadx=10, ipady=0, padx=2, pady=10, side="left")
        # rbnbtn_5.pack(ipadx=10, ipady=0, padx=2, pady=10, side="left")
        # rbnbtn_6.pack(ipadx=10, ipady=0, padx=30, pady=10, side="right")
        for btn in rbnbtns:
            btn.pack(ipadx=10, ipady=0, padx=4, pady=10, side="left")

        rbncanv_1.pack(padx=20, pady=0, side="left")
        rbncanv_2.pack(padx=20, pady=0, side="left")
        rbncanv_3.pack(padx=20, pady=0, side="left")

        rbnfrme_date.grid(column=0, row=0, padx=30, pady=10, sticky="news")
        rbnfrme_btn.grid(column=1, row=0, sticky="news")
        rbnfrme_stat.grid(column=0, row=1, columnspan=2, sticky="news")

        # Data frame Elements
        data_frame_canvases.rowconfigure(0, weight=1)
        data_frame_canvases.rowconfigure(1, weight=1)
        data_frame_canvases.columnconfigure(0, weight=4)
        data_frame_canvases.columnconfigure(1, weight=3)

        # data_canv1 = tk.Canvas(data_frame_canvases, width=200, height=200, bd=0, relief="solid", highlightbackground="#222", highlightthickness=2)
        # data_canv2 = tk.Canvas(data_frame_canvases, width=200, height=200, bd=0, relief="solid", highlightbackground="#222", highlightthickness=2)
        # data_canv3 = tk.Canvas(data_frame_canvases, width=100, height=200, bd=0, relief="solid", highlightbackground="#222", highlightthickness=2)
        # data_canv4 = tk.Canvas(data_frame_canvases, width=100, height=200, bd=0, relief="solid", highlightbackground="#222", highlightthickness=2)
        data_canv1 = self.CreateDataPill(data_frame_canvases, "", "Anomaly Detected")
        data_canv2 = self.CreateDataPill(data_frame_canvases, "", "Audio Detected")

        data_canv1.grid(column=0, row=0, sticky="nw")
        data_canv2.grid(column=0, row=1, sticky="nw")
        # data_canv3.grid(column=1, row=0, sticky="nw")
        # data_canv4.grid(column=1, row=1, sticky="nw")

        # Data frame internal frame positioning
        data_frame_menu.grid(column=0, row=0, padx=0, pady=0, sticky="new")
        data_frame_ribbon.grid(column=0, row=1, padx=0, pady=0, sticky="nsew")
        data_frame_canvases.grid(column=0, row=2, padx=0, pady=0, sticky="news")

        # Positioning frames within window
        sidebar_frame.grid(column=0, row=0, columnspan=1, rowspan=1, padx=0, pady=0, sticky="news")
        data_frame.grid(column=1, row=0, columnspan=2, rowspan=1, padx=0, pady=0, sticky="news")
    
    def show(self):
        self.root.mainloop()

    def closeWindow(self):
        self.root.close()
    
    def CreateStatPill(self, parent, imgpath="", title="Pill", width=300, height=50, font=None, value=""):
        container = tk.Frame(parent, bg="#7ef", bd=2)
        lbl = tk.Label(container, text=title)
        canv = tk.Canvas(container, height=50, width=50, bd=0, highlightbackground="#222", highlightthickness=2)
        if(imgpath is not None):
            img= tk.PhotoImage(file=imgpath)
            canv.create_image(50, 50, anchor=tk.NW, image=img)
        
        canv.pack(padx=2, pady=2, side="left")
        lbl.pack(padx=20, pady=0, side="left")

        return container

    def CreateDataPill(self, parent, imgpath="", title="Pill", width=300, height=50, font=None):
        container = tk.Frame(parent, bd=2)
        lbl = tk.Label(container, text=title)
        canv = tk.Canvas(container, height=100, width=500, bd=0, highlightbackground="#222", highlightthickness=2)
        
        lbl.pack(padx=20, pady=0)
        canv.pack(padx=2, pady=2)

        return container

    def CreateButtonArray(self, parent, count=0, titles=[], commands=[], anchor="left"):
        output = []
        for i in range(count):
            output.append(tk.Button(parent, text=titles[i]))

        return output

