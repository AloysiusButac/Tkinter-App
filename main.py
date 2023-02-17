import tkinter as tk

import Window_App as win

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MVC Demo')

        # create a model
        # model = Model('hello@pythontutorial.net')

        # create a view and place it on the root window
        # view = View(self)
        # view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        # controller = Controller(model, view)

        # set the controller to view
        # view.set_controller(controller)

        win1 = win.Window1(self)
        win1.show()


if __name__ == '__main__':
    # w = win.Window1(tk.Tk())
    # w.show()
    app = App()
    app.mainloop()