import tkinter as tk
from welcome_page import WelcomePage
from counter_page import CounterPage
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Modular Tkinter App")
        self.frames = {}
        self.frames[WelcomePage] = lambda: WelcomePage(self)
        self.frames[CounterPage] = lambda: CounterPage(self)
        self.show_frame(WelcomePage)

    def show_frame(self, container):
        frame = self.frames[container]()
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
