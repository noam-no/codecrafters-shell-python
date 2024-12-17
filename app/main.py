import sys

commands = {}


def invalid_command(input):
    if input not in commands:
        print(f"{input}: command not found")

def main():
    sys.stdout.write("$ ")

    # Wait for user input
    command = input()
    invalid_command(command)


if __name__ == "__main__":
    main()
