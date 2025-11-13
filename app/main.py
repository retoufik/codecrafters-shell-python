import os
import sys
import shutil
import subprocess

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
                    builtins = {"echo", "type", "exit"}
                    for arg in args:
                        if arg.lower() in builtins:
                            print(f"{arg} is a shell builtin")
                            continue

                        found_path = shutil.which(arg)
                        if found_path:
                            print(f"{arg} is {found_path}")
                        else:
                            print(f"{arg}: not found")
            else:
                parts = command.strip().split()
                if not parts:
                    continue
                cmd = parts[0]
                cmd_args = parts[1:]

                # find executable in PATH (handles PATHEXT on Windows)
                found_path = shutil.which(cmd)
                if found_path:
                    # run the program and let its output go to the shell's stdout/stderr
                    # use 'executable' so argv[0] stays as the typed command name
                    try:
                        subprocess.run([cmd] + cmd_args, executable=found_path)
                    except FileNotFoundError:
                        sys.stdout.write(f"{cmd}: not found\n")
                    except Exception as e:
                        sys.stdout.write(f"{cmd}: {e}\n")
                else:
                    sys.stdout.write(f"{cmd}: not found\n")
            continue
        break


if __name__ == "__main__":
    main()
