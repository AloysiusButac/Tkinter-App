import tkinter as tk

import Window_App as win

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MVC Demo')

        window_manager = win.WindowManager(self)
        model = win.MyVideoCapture(0)

        self.controller = win.Controller(model, window_manager)

        # win1 = win.Window1(self)
        # win1.SetStream1(win.MyVideoCapture("1.gif", name="test1"))
        # win1.SetStream2(win.MyVideoCapture("2.gif", name="test2"))
        # win1.SetStream3(win.MyVideoCapture("3.gif", name="test3"))
        # win1.SetStream4(win.MyVideoCapture("4.gif", name="test4"))
        # win1.show()

if __name__ == '__main__':
    app = App()
    # app.mainloop()

"""
multiple camera recording: https://gist.github.com/aarmea/629e59ac7b640a60340145809b1c9013
                         : https://stackoverflow.com/questions/58592291/how-to-capture-multiple-camera-streams-with-opencv#:~:text=To%20capture%20multiple%20streams%20with,VideoCapture().
saving video: https://stackoverflow.com/questions/29317262/opencv-video-saving-in-python/71624807#71624807
"""
