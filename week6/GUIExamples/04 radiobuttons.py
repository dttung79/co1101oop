import tkinter as tk


def clicked():
    res = f"You have selected {values[selected.get()]}"
    output.set(res)


window = tk.Tk()
window.geometry("300x50")
window.title("GUI Example")

selected = tk.IntVar(window)
selected.set(1)
values = ["zero", "one", "two"]
for i in range(len(values)):
    rad = tk.Radiobutton(window, text=values[i], value=i, variable=selected)
    rad.grid(column=i, row=0)

btn = tk.Button(window, text="Click Me", command=clicked)
btn.grid(column=0, row=1)

output = tk.StringVar(window)
txt = tk.Entry(window, width=30, textvariable=output, state="readonly")
txt.grid(column=1, row=1, columnspan=2)

window.mainloop()
