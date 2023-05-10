def chosen(device, command):
    if device in command or device.replace(" ", "") in command:
        return True
    else:
        return False

def init_devices():
    device_names = ['heating', 'light', 'music player']
    device_ons = [False, False, False]
    device_settings = [20, 200, 10]
    device_types = ['temperature', 'brightness', 'volume']
    
    for device in device_names:
        print(f"{device} has been initialised")

    return device_names, device_ons, device_settings, device_types

def init_name():
    name = input("What is your name? ")
    print(f"Hello {name}")
    return name

def control_device(name, device_names, device_ons, device_settings, device_types, 
                                                                    command, device):
    i = device_names.index(device)
    if " on " in command:
        device_ons[i] = True
        print(device + " is on")
    elif " off " in command:
        device_ons[i] = False
        print(device + " is off")
    elif " up " in command:
        device_settings[i] += 1
        print(f" {device} {device_types[i]} is set to {device_settings[i]}")
    elif " down " in command:
        device_settings[i] -= 1
        print(f" {device} {device_types[i]} is set to {device_settings[i]}")
    elif " play " in command and device == "music player":
        print(f" {device} is playing")
    elif " pause " in command and device == "music player":
        print(f" {device} is paused")
    else:
        print(f"Sorry {name}, I do not understand that")

def main():
    device_names, device_ons, device_settings, device_types = init_devices()
    name = init_name()

    while True:
        print()
        command = input(f"What next, {name}? ")
        command = f" {command.lower()} "

        if "system off" in command:
            break

        device_chosen = None
        for device in device_names:
            if chosen(device, command):
                device_chosen = device
                break

        if device_chosen is None:
            print(f"Sorry {name}, I do not understand that")
        else:
            control_device(name, device_names, device_ons, device_settings, command, device)

    print(f"Bye bye, {name}")


### Main starts here
main()