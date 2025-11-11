import sys
import string

def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command.strip().lower() != "exit 0":
            print(f"{command}: command not found")
            continue
        break


if __name__ == "__main__":
    main()
