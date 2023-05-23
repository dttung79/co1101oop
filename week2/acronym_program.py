# Write a program to work with acronyms.
# The program asks user to enter an acronym then prints the full name of the acronym then loops back to ask for another acronym.
# If user enter a dot (.), the program will print all the acronyms and their full names.
# If user enter a word 'quit', the program will exit.
# If user enter a new acronym, the program will ask if user wants to add this new acronym to the dictionary. If user choose yes then ask for the full name of the acronym then store it in the dictionary.

# create a dictionary of acronyms
# HW: instead a fix dictionary, read the dictionary from a file (acronyms.txt)
def init_acronyms():
    acronyms_dict = {
        'IP': 'Internet Protocol', 
        'DNS': 'Domain Name Service', 
        'RAM': 'Random Access Memory' 
    }
    return acronyms_dict

def print_acronyms(acronyms_dict):
    for key in acronyms_dict:
        print(key, ':', acronyms_dict[key])

def handle_new_acronym(acronyms_dict, acronym):
    answer = input('This is a new acronym. Do you want to add it to the dictionary? (y/n) ')
    if answer == 'y':
        full_name = input('Enter the full name of the acronym: ')
        acronyms_dict[acronym] = full_name
        print('Acronym added!')


### MAIN PROGAM ###
acronyms_dict = init_acronyms()
running = True
while running:
    acronym = input('Enter an acronym: ')
    if acronym == '.':
        print_acronyms(acronyms_dict)
    elif acronym == 'quit':
        print('Program quits!')
        running = False
    elif acronym in acronyms_dict:
        print(acronym, ':', acronyms_dict[acronym])
    else:
        handle_new_acronym(acronyms_dict, acronym)
