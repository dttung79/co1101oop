import tkinter as tk


def clicked():
    if chk_state.get():
        res = "Checkbox is checked"
    else:
        res = "Checkbox is not checked"
    output.set(res)


window = tk.Tk()
window.geometry("300x50")
window.title("GUI Example")

chk_state = tk.BooleanVar(window, True)
chk = tk.Checkbutton(window, text="Choose", var=chk_state)
chk.grid(column=0, row=0)

btn = tk.Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)

output = tk.StringVar(window)
txt = tk.Entry(window, width=30, textvariable=output, state="readonly")
txt.grid(column=2, row=0)

window.mainloop()
