from enum import Enum
import cv2
from VideoCapture import *

class State(Enum):
    WINDOW1 = 1
    WINDOW2 = 2

# VideoCapture serves as out model
# Window Manager serves as our view

class Controller:
    model = None
    viewManager = None
    def __init__(self, master, model, viewmanager):
        print("Controller initialized")
        self.model = model
        self.viewManager = viewmanager
        self.master = master

        self.state = State.WINDOW1
        self.viewManager.OpenWindow1()
        self.viewManager.OpenWindow2()
    
    def show(self):
        self.master.mainloop()

    def update(self):
        # self.view.update()
        pass
    
    def change_state(self, state):
        self.state = state
    
    def save_recording(self):
        pass

    def save_video(self):
        pass
