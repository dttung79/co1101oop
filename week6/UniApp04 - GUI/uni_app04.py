import tkinter as tk
import tkinter.ttk as ttk

import database04 as db

users = db.get_users()

# print out all the user details
for user in users:
    print(f"name:      {user.name}")
    if hasattr(user, "user_id"):
        print(f"user id:   {user.user_id}")
    if hasattr(user, "job"):
        print(f"job title: {user.job}")
    if hasattr(user, "programme"):
        print(f"programme: {user.programme}")
    if hasattr(user, "modules"):
        for module in user.modules:
            print(f" {module}")
    print()


def clicked():
    group = combo.get()
    print(f"To:      {group}")
    message = message_txt.get()
    print(f"Message: {message}")
    for user in users:
        send_message = False
        if group == "all":
            send_message = True
        elif group == "students":
            if hasattr(user, "programme"):
                send_message = True
        elif group == "staff":
            if hasattr(user, "job"):
                send_message = True
        else:  # group is a module
            if hasattr(user, "modules") and group in user.modules:
                send_message = True
        if send_message:
            print(f" '{message}' sent to {user.name}")
    print()


window = tk.Tk()
window.geometry("400x60")
window.title("Uni App")

groups = ["", "all", "staff", "students"]
for user in users:
    if hasattr(user, "modules"):
        for module in user.modules:
            if module not in groups:
                groups.append(module)

combo = ttk.Combobox(window)
combo["values"] = groups
combo.current(0)
combo.grid(column=0, row=0)

btn = tk.Button(window, text="Send message", command=clicked)
btn.grid(column=1, row=0)

message_txt = tk.Entry(window, width=60)
message_txt.grid(column=0, row=1, columnspan=2, padx=15, pady=5)

window.mainloop()
