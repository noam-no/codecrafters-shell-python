#!/usr/bin/env python3

import sys, re, signal

def signal_handler(sig, frame):
    print("")
    sys.stdout.write("$ ")
    sys.stdout.flush()

def exit_command(args):
    print("exit")
    if len(args) == 0:
        pass
    
    elif re.match(r"\D",args[0]) != None:
        print(f"bash: exit: {args[0]}: numeric argument required")
        args[0] = 0
    
    elif len(args) > 1:
        print("bash: exit: too many arguments")
        return
    
    sys.exit(int(args[0]))


commands = {"exit": exit_command}

def command_parser(raw_input):
    command = raw_input.split()
    if not command:
        return
    header = command[0]
    if header not in commands:
        print(f"{header}: command not found")
    else:
        commands[header](command[1:])

def main():
    while True:
        try:
            signal.signal(signal.SIGINT, signal_handler)
            sys.stdout.write("$ ")
            sys.stdout.flush()

            # Wait for user input
            command = input()
            command_parser(command)
        except EOFError:
            print("")
            exit_command(["1"])

if __name__ == "__main__":
    main()
