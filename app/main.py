import sys
import string

def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command.strip().lower() != "exit 0":
            if command.strip().lower().split()[0]== "echo":
                    args = command.strip().split()[1:]
                    print(" ".join(args))
            else:
                sys.stdout.write(f"{command} : Command not found\n")
        continue
        break


if __name__ == "__main__":
    main()
