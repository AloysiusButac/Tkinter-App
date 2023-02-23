from window1 import *
from window2 import *
import Window_App as window_app

class WindowManager:

    window_stack = []

    def __init__(self, parent):
        print("Window manager created!")

        self.parent = parent

        window_1 = Window1(self.parent)

        # self.window_stack.append(window_1)
        self.window_stack.append(Window1(self.parent))
        self.window_stack[0].SetStream1(window_app.MyVideoCapture("1.gif", name="test1"))
        self.window_stack[0].SetStream2(window_app.MyVideoCapture("2.gif", name="test2"))
        self.window_stack[0].SetStream3(window_app.MyVideoCapture("3.gif", name="test3"))
        self.window_stack[0].SetStream4(window_app.MyVideoCapture("4.gif", name="test4"))
        # self.window_stack.append(Window2(self.parent))

        self.active_window = 0
    
    def OpenWindow1(self):
        self.active_window = 0
        self.show()

    def OpenWindow2(self):
        self.active_window = 1
        self.show()

    def show(self):
        for i in range(len(self.window_stack)):
            if self.active_window == i:
                continue
            self.window_stack[i].withdraw()

        self.window_stack[self.active_window].update()
        self.window_stack[self.active_window].deiconify()
