import sys

commands = {}


def invalid_command(input):
    if input not in commands:
        print(f"{input}: command not found")
        

def main():
    try:
        while True:
            sys.stdout.write("$ ")

            # Wait for user input
            command = input()
            invalid_command(command)
    
    
    
    
    
    except KeyboardInterrupt:
        print("\nExiting shell ...")

if __name__ == "__main__":
    main()
