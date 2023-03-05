import tkinter as tk

import Window_App as win

class DataModel:
    def __inti__(self):
        pass

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MVC Demo')

        window_manager = win.WindowManager(self)
        model = DataModel()

        self.controller = win.Controller(self, model, window_manager)

if __name__ == '__main__':
    app = App()
    app.mainloop()

"""
multiple camera recording: https://gist.github.com/aarmea/629e59ac7b640a60340145809b1c9013
                         : https://stackoverflow.com/questions/58592291/how-to-capture-multiple-camera-streams-with-opencv#:~:text=To%20capture%20multiple%20streams%20with,VideoCapture().
saving video: https://stackoverflow.com/questions/29317262/opencv-video-saving-in-python/71624807#71624807
"""
