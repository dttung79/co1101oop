import tkinter as tk


def clicked():
    lbl.configure(text="Button was clicked!")


window = tk.Tk()
window.geometry("300x50")
window.title("GUI Example")

btn = tk.Button(window, text="Click Me", command=clicked)
btn.grid(column=0, row=0)

lbl = tk.Label(window, text="Hello")
lbl.grid(column=1, row=0)

window.mainloop()
