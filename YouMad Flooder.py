import importlib
import os
import sys
from time import sleep

from colorama import init
from termcolor import colored, cprint

init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected


def load_modules():
    plugins_dict = {}
    directory = './plugins'
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            filename = filename[:-3]
            globals()[filename] = importlib.import_module(
                f"plugins.{filename}"
            )
            plugins_dict[filename] = globals()[filename]

    return plugins_dict


def choose_an_option(plugins_dict):

    cprint("|--> Choose an option", color="red", attrs=['bold'])
    x = 1
    for item in plugins_dict:
        cprint(f"|   {x}.--> {item} bombing", color="red", attrs=['bold'])
        x = x + 1
    cprint("|", color="red", attrs=['bold'])
    option = input(colored("$--> ", color="red", attrs=['bold']))
    if option.isdigit():
        x = 1
        for item in plugins_dict:
            if x == int(option):
                return item
            x = x + 1
        return None
    else:
        x = 1
        option = option.split(" ")
        option = option[0].replace(".", "")
        for item in plugins_dict:
            if option.lower() == item.lower():
                return item
            x = x + 1
        return None


def init():
    os.system('cls||clear')

    cprint(""" 
    | ░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄ 
    | ░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄
    | ░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█        __   _____  _   _   __  __    _    ____   
    | ░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░█        \ \ / / _ \| | | | |  \/  |  / \  |  _ \  
    | ░▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░█        \ V / | | | | | | | |\/| | / _ \ | | | | 
    | █▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒█        | || |_| | |_| | | |  | |/ ___ \| |_| | 
    | █▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█       |_| \___/ \___/  |_|  |_/_/   \_\____/  
    | ░█▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█       _____ _     ___   ___  ____  _____ ____  
    | ░░█░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█       |  ___| |   / _ \ / _ \|  _ \| ____|  _ \ 
    | ░░░█░░██░░▀█▄▄▄█▄▄█▄████░█         | |_  | |  | | | | | | | | | |  _| | |_) |
    | ░░░░█░░░▀▀▄░█░░░█░███████░█        |  _| | |__| |_| | |_| | |_| | |___|  _ <
    | ░░░░░▀▄░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█        |_|   |_____\___/ \___/|____/|_____|_| \_\ 
    | ░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░█         
    | ░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░█
    | ░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░█
    |      
    |
    |--> Check the repository on https://github.com/TallGorilla/YouMad-Flooder""", color="red", attrs=['bold'])

    sleep(1)
    os.system('cls||clear')

    plugins_dict = load_modules()

    option = choose_an_option(plugins_dict)
    while not option:
        os.system('cls||clear')
        cprint(
            "|--> Invalid option, please try again.",
            color="red",
            attrs=['bold']
        )
        sleep(1)
        os.system('cls||clear')
        option = choose_an_option()
    os.system('cls||clear')
    plugins_dict[option].init()
    os.system('cls||clear')
    cprint(
        "|--> Thanks for using YouMadFlooder!",
        color="red",
        attrs=['bold']
    )
    input(colored("$--> Press return to exit.", color="red", attrs=['bold']))


if __name__ == "__main__":
    init()
