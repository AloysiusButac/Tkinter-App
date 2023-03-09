from window1 import *
from window2 import *
import Window_App as window_app

class WindowManager:
    window_stack = []

    def __init__(self, parent, no_of_windows=2):
        print("Window manager created!")
        self.root = parent

        self.setLogo("BantAI.png")

        self.main_window = window_app.MainWindow(self.root)

    def OpenWindow1(self):
        self.main_window.SetStream1(MyVideoCapture("1.gif", name="test1"))
        self.main_window.SetStream2(MyVideoCapture("2.gif", name="test2"))
        self.main_window.SetStream3(MyVideoCapture("3.gif", name="test3"))
        self.main_window.SetStream4(MyVideoCapture("4.gif", name="test4"))
        self.main_window.setMenuButtonCommand(self.OpenWindow2)
        self.main_window.update()

    def OpenWindow2(self):
        # Create window 2
        self.second_window = Toplevel(self.root)
        self.second_window.geometry("{}x{}+{}+{}".format(self.root.winfo_width(), self.root.winfo_height(), 100, 100))
        self.second_window.title("Window2")
        # Create window 2 content
        self.second_window_frame = window_app.Window2(self.second_window).get_window()
        self.second_window_frame.pack(fill="both", expand=True)
        # Change Logo
        self.second_window.iconphoto(False, self.logo)

        print('Window2 opened.')

    # ==================== HELPERS ==================== 
    def setLogo(self, logo_path):
        self.logo = PhotoImage(file = logo_path)
        self.root.iconphoto(False, self.logo)
    
