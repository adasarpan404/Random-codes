import tkinter as tk
from counter_page import CounterPage


class WelcomePage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        tk.Label(self, text="Welcome to our Tkinter App!").pack()
        tk.Button(self, text="Go to Counter Page",
                  command=lambda: master.show_frame(CounterPage)).pack()
