from light import Light
from heating import Heating
from music import MusicPlayer

def chosen(device, command):
    if device in command or device.replace(" ", "") in command:
        return True
    else:
        return False

def init_devices():
    light = Light()
    heating = Heating()
    music_player = MusicPlayer()
    devices = [light, heating, music_player]

    for device in devices:
        print(f"{device.name} has been initialised")
    
    return devices


def init_name():
    name = input("What is your name? ")
    print(f"Hello {name}")
    return name

def control_device(name, device, command):
    if ' on ' in command:
        device.turn_on()
    elif ' off ' in command:
        device.turn_off()
    elif ' up ' in command:
        device.increase()
    elif ' down ' in command:
        device.decrease()
    elif ' play ' in command and device.name == 'Music Player':
        device.play()
    elif ' pause ' in command and device.name == 'Music Player':
        device.pause()
    elif ' next ' in command and device.name == 'Music Player':
        device.next()
    elif ' previous ' in command and device.name == 'Music Player':
        device.previous()
    else:
        print(f"Sorry {name}, I do not understand {command}")

## main program
def main():
    devices = init_devices()
    name = init_name()
    while True:
        print()
        command = input(f"What next, {name}? ")
        command = f" {command.lower()} "
        if "system off" in command:
            break
        for device in devices:
            if chosen(device.name.lower(), command):
                control_device(name, device, command)

main()