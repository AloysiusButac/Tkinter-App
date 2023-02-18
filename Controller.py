from enum import Enum
import cv2
from VideoCapture import *

class State(Enum):
    WINDOW1 = 1
    WINDOW2 = 2

# VideoCapture serves as out model
# Active window(window1/window2) serves as our view

class Controller:
    def __init__(self, model, view):
        print("Controller initialized")
        self.model = model
        self.view = view

        # self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')

        self.state = State.WINDOW1

    def update(self):
        self.view.update()
    
    def change_state(self, state):
        self.state = state
    
    def setCamGrid(self, streams=[MyVideoCapture()]*4):
        self.model
    
    def save_recording(self):
        pass

    def save_video(self):
        pass

    def setStream(self, stream, index=0, window1=True):
        if window1:
            if index == 1:
                self.view.SetStream1(stream)
            elif index == 2:
                self.view.SetStream2(stream)
            elif index == 3:
                self.view.SetStream3(stream)
            elif index == 4:
                self.view.SetStream4(stream)
            else:
                print("Controller Set stream index error.")
        else:
            print("Trying to stream to window other than window 1.")