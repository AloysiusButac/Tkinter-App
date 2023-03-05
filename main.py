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

