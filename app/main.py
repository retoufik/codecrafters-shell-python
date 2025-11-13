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
                    args = command[5:].strip()
                    if args.startswith('"') and args[-1].endswith('"') or args.startswith("'") and args[-1].endswith("'"):
                        args = args[1:-1]
                        for arg in args:
                            if arg=="'" or arg =='"':
                                args = args.replace(arg, "")
                        print(args)
                    else:
                        hint = False
                        for arg in args:
                            if arg=="'" or arg =='"':
                                args = args.replace(arg, "")
                                hint = True
                        if hint:
                            print(args)
                        else:
                            args_split = args.split()
                            print(" ".join(args_split))
            elif command.strip().lower().split()[0] == "cat":
                args = command[3::].strip()
                if args.startswith('"') and args[-1].endswith('"') or args.startswith("'") and args[-1].endswith("'"):
                    args = args[1:-1]
                    for arg in args:
                        if arg=="'" or arg =='"':
                            args = args.replace(arg, "")
                    try:
                        with open(args, 'r') as f:
                            sys.stdout.write(f.read())
                    except FileNotFoundError:
                        sys.stdout.write(f"cat: {args}: No such file or directory\n")
                    except Exception as e:
                        sys.stdout.write(f"cat: {e}\n")
                else:
                    args_split = args.split()
                    for file_name in args_split:
                        try:
                            with open(file_name, 'r') as f:
                                sys.stdout.write(f.read())
                        except FileNotFoundError:
                            sys.stdout.write(f"cat: {file_name}: No such file or directory\n")
                        except Exception as e:
                            sys.stdout.write(f"cat: {e}\n")
            elif command.strip().lower().split()[0] == "type":
                    args = command.strip().split()[1:]
                    builtins = {"echo", "type", "exit","pwd","cd","cat"}
                    for arg in args:
                        if arg.lower() in builtins:
                            print(f"{arg} is a shell builtin")
                            continue

                        found_path = shutil.which(arg)
                        if found_path:
                            print(f"{arg} is {found_path}")
                        else:
                            print(f"{arg}: not found")
            elif command.strip().lower().split()[0] == "pwd":
                print(os.getcwd())
            elif command.strip().lower().split()[0] == "cd":
                args = command.strip().split()[1:]
                if len(args) == 0:
                    target_dir = os.path.expanduser("~")
                elif args[0] == "~":
                    target_dir = os.getenv("HOME")
                else:
                    target_dir = args[0]
                try:
                    os.chdir(target_dir)
                except FileNotFoundError:
                    sys.stdout.write(f"cd: {target_dir}: No such file or directory\n")
                except Exception as e:
                    sys.stdout.write(f"cd: {e}\n")
            else:
                parts = command.strip().split()
                if not parts:
                    continue
                exe = parts[0]
                exe_args = parts[1:]
                found_path = shutil.which(exe)
                if found_path:
                    try:
                        subprocess.run([exe] + exe_args, executable=found_path)
                    except FileNotFoundError:
                        sys.stdout.write(f"{exe}: not found\n")
                    except Exception as e:
                        sys.stdout.write(f"{exe}: {e}\n")
                else:
                    sys.stdout.write(f"{exe}: not found\n")
            continue
        break


if __name__ == "__main__":
    main()
