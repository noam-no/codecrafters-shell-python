#!/usr/bin/env python3

# Importing libraries
from sys import exit, stdout
from os import getcwd, environ, path, listdir
from re import match
from signal import signal, SIGINT
from getpass import getuser
from socket import gethostname
try:
    from .ansi_customization import ANSI_CHAR, graphics_text_parser
except (ModuleNotFoundError, ImportError) as exceptions:
    from ansi_customization import ANSI_CHAR, graphics_text_parser
# Constants
# To use later codecrafter doesn't like it for now ...
"""
USERNAME = getuser()
MACHINE_USERNAME = graphics_text_parser(USERNAME+'@'+gethostname(), "BOLD", "BRIGHT_GREEN")
PWD = graphics_text_parser(getcwd().replace(f"/home/{USERNAME}", "~"), "BOLD", "BRIGHT_BLUE")
SHELL_PROMPT = f"{MACHINE_USERNAME+':'+PWD}$ "
"""


PATH = environ["PATH"].split(":") # PATH of the system for binaries
SHELL_PROMPT = "$ "
EXIT_CODE_DEFAULT = 0
EXIT_CODE_ERROR = 1
COMMANDS = {"exit": None,
            "echo": None,
            "type": None}

BUILT_IN = ["exit", "echo", "type"]

def exit_command(args):
    print("exit")
    if len(args) == 0:
        args.append(0)
        
    
    elif match(r"\D",args[0]) != None:
        print(f"bash: exit: {args[0]}: numeric argument required")
        args[0] = 0
    
    elif len(args) > 1:
        print("bash: exit: too many arguments")
        return
    
    exit(int(args[0]))

def echo_command(args):
    print(" ".join(args))

def type_command(args):
    if len(args) > 0:
        for arg in args:
            if arg in BUILT_IN:
                print(f"{arg} is a shell builtin")
            else:
                for p in PATH:
                    try:
                        binaries = [f for f in listdir(p) if path.isfile(path.join(p, f))]
                    except FileNotFoundError:
                        pass
                    if arg in binaries:
                        print(f"{arg} is {path.join(p, arg)}")
                        return
                print(f"bash: type: {arg}: not found")

COMMANDS.update({
                "exit": exit_command,
                "echo": echo_command,
                "type": type_command,
                
                })

def command_parser(raw_input):
    command = raw_input.split()
    if not command:
        return
    header = command[0]
    if header not in COMMANDS:
        print(f"{header}: command not found")
    else:
        COMMANDS[header](command[1:])

# Intercepts the SIGINT signal (Ctrl+C)
def signal_handler(sig, frame):
    print("")
    stdout.write(SHELL_PROMPT)
    stdout.flush()

def main():
    while True:
        try:
            signal(SIGINT, signal_handler)
            stdout.write(SHELL_PROMPT)
            stdout.flush()

            # Wait for user input
            command = input()
            command_parser(command)
        except EOFError:
            print("")
            exit_command(["1"])

if __name__ == "__main__":
    main()
