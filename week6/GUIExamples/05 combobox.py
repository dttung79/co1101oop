import tkinter as tk
import tkinter.ttk as ttk


def clicked():
    res = f"You have selected {combo.get()}"
    output.set(res)


window = tk.Tk()
window.geometry("350x50")
window.title("GUI Example")

combo = ttk.Combobox(window)
combo["values"] = ["zero", "one", "two", "three", "four"]
combo.current(1)
combo.grid(column=0, row=0)

btn = tk.Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)

output = tk.StringVar(window)
txt = tk.Entry(window, width=30, textvariable=output, state="readonly")
txt.grid(column=2, row=0)

window.mainloop()
