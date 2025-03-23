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
            #command = command.replace("type","").strip()
            print(f"{command[5:]} is a shell builtin")
        elif "echo" in command:
            #command = command.replace("echo","").strip()
            print(f"{command[5:]}")
        else:
            print(f"{command}: command not found")



if __name__ == "__main__":
    main()
