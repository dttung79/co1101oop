import tkinter as tk
from tkinter import simpledialog

from heating05 import Heating
from light05 import Light
from musicplayer05 import MusicPlayer
from spotlight05 import SpotLight


def chosen(device, command):
    if device.name in command or device.name.replace(" ", "") in command:
        return True
    else:
        return False


ceiling_light = Light("ceiling light")
floor_lamp = Light("floor lamp")
table_lamp = Light("table lamp")
spot_light = SpotLight()
music_player = MusicPlayer()
heating = Heating()

devices = [ceiling_light, floor_lamp, table_lamp, spot_light, music_player, heating]


def respond(event):
    print()
    command = f" {input_txt.get().lower()} "

    if "system off" in command:
        exit()

    device_chosen = None
    for device in devices:
        if chosen(device, command):
            device_chosen = device
            break

    if device_chosen is None:
        print(f"Sorry {name}, I do not understand that")
    else:
        if " on " in command:
            device_chosen.switch_on()
        elif " off " in command:
            device_chosen.switch_off()
        elif " up " in command and hasattr(device_chosen, "up"):
            device_chosen.up()
        elif " down " in command and hasattr(device_chosen, "down"):
            device_chosen.down()
        elif " play " in command and hasattr(device_chosen, "play"):
            device_chosen.play()
        elif " pause " in command and hasattr(device_chosen, "pause"):
            device_chosen.pause()
        else:
            print(f"Sorry {name}, I do not understand that")


window = tk.Tk()
window.withdraw()
name = simpledialog.askstring("?", "What is your name?", parent=window)

window = tk.Tk()
window.geometry("400x320")
window.title(f"{name}'s Home Hub")
window.after(1, lambda: window.focus_force())  # trickery to focus on the main window

row = 0
input_txt = tk.Entry(window, width=60)
input_txt.grid(column=0, row=row, columnspan=4, padx=15, pady=5)
input_txt.bind('<Return>', respond)

for device in devices:
    row += 1
    label = tk.Label(window, text=device.name)
    label.grid(column=0, row=row, sticky="W", padx=15, pady=10)
    radio_setting = tk.IntVar(window)
    radio_setting.set(0)
    values = ["off", "on"]
    for i in range(2):
        radio_button = tk.Radiobutton(window, text=values[i], value=i, variable=radio_setting, state=tk.DISABLED)
        radio_button.grid(column=i + 1, row=row, sticky="W")
    if hasattr(device, "setting"):
        slider = tk.Scale(window, from_=0, to=device.maximum, orient=tk.HORIZONTAL)
        slider.grid(column=3, row=row, sticky="W")
        device.set_widgets(radio_setting, slider)
    else:
        device.set_widget(radio_setting)

window.mainloop()
