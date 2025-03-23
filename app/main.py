import sys


def main():
    x = True
    while x == True:
        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        if command == "exit 0":
            x = False
        elif "type" in command:
            if command[5:] == "type" or command[5:] == "echo" or command[5:] == "exit":
                print(f"{command[5:]} is a shell builtin")
            else:
                print(f"{command[5:]}: not found")
        elif "echo" in command:
            print(f"{command[5:]}")
        else:
            print(f"{command}: command not found")



if __name__ == "__main__":
    main()
