import tkinter as tk


def clicked():
    res = "Hello " + input_txt.get()
    output.set(res)


window = tk.Tk()
window.geometry("300x50")
window.title("GUI Example")

input_txt = tk.Entry(window, width=10)
input_txt.focus()
input_txt.grid(column=0, row=0)

btn = tk.Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)

output = tk.StringVar(window)
txt = tk.Entry(window, width=30, textvariable=output, state="readonly")
txt.grid(column=2, row=0)

window.mainloop()
