import sys
import string

def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command.strip().lower() != "exit 0":
            if command.strip().lower().split()[0] == "echo":
                    args = command.strip().split()[1:]
                    print(" ".join(args))
            elif command.strip().lower().split()[0] == "type":
                    args = command.strip().split()[1:]
                    for arg in args:
                        if arg.lower() in ["echo", "type", "exit"]:
                            print(f"{arg} is a shell builtin")
                        else:
                            print(f"{arg}: not found")
            else:
                sys.stdout.write(f"{command}: command not found\n")
            continue
        break


if __name__ == "__main__":
    main()
