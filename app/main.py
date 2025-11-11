import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    sys.stdout.write("$ ")
    command = input()
    print(f"{command}: command does not exist, Try again")

if __name__ == "__main__":
    main()
