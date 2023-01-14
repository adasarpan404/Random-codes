import tkinter as tk

class CounterPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.counter = 0
        self.label = tk.Label(self, text="Counter: 0")
        self.label.pack()

        tk.Button(self, text="Increment", command=self.increment_counter).pack()
    def increment_counter(self):
        self.counter += 1
        self.label.config(text="Counter: {}".format(self.counter))
