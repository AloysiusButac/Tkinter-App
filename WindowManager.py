from window1 import *
from window2 import *
import Window_App as window_app

class WindowManager:

    window_stack = []

    def __init__(self, parent, no_of_windows=2):
        print("Window manager created!")

        self.root = parent
        self.main_window = window_app.Window1(self.root)
        self.main_window.SetStream1(MyVideoCapture("1.gif", name="test1"))
        self.main_window.SetStream2(MyVideoCapture("2.gif", name="test2"))
        self.main_window.SetStream3(MyVideoCapture("3.gif", name="test3"))
        self.main_window.SetStream4(MyVideoCapture("4.gif", name="test4"))
        #  self.window_stack.append(main_window)
        self.main_window.setMenuButtonCommand(self.OpenWindow2)
    
    def OpenWindow1(self):
        pass

    def OpenWindow2(self):
        # self.second_window = Toplevel(self.root)
        # win = window_app.Window2(self.main_window)
        print('Window2 opened.')