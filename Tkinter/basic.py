import tkinter as tk

def on_button_click():
    global counter
    counter += 1
    label.config(text="Counter: " + str(counter))

root = tk.Tk()
counter = 0

label = tk.Label(root, text="Counter: 0")
label.pack()

button = tk.Button(root, text="Increment", command=on_button_click)
button.pack()

root.mainloop()

