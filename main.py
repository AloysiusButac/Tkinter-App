import tkinter as tk

import Window_App as win

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MVC Demo')

        win1 = win.Window2(self)
        # win1.SetStream1(win.MyVideoCapture(0))
        # win1.SetStream2(win.MyVideoCapture("sample.mkv"))
        # win1.SetStream3(win.MyVideoCapture("1.gif"))
        # win1.SetStream4(win.MyVideoCapture("2.gif"))
        win1.show()

if __name__ == '__main__':
    app = App()
    app.mainloop()