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
                    raw = command[5:].lstrip()
                    args = []
                    cur = []
                    i = 0
                    n = len(raw)
                    in_single = False
                    in_double = False
                    while i < n:
                        ch = raw[i]
                        if ch == "'" and not in_double:
                            in_single = not in_single
                            i += 1
                            continue
                        if ch == '"' and not in_single:
                            in_double = not in_double
                            i += 1
                            continue
                        if ch.isspace() and not in_single and not in_double:
                            if cur:
                                args.append(''.join(cur))
                                cur = []
                            # skip consecutive spaces
                            while i < n and raw[i].isspace():
                                i += 1
                            continue
                        cur.append(ch)
                        i += 1
                    if cur:
                        args.append(''.join(cur))

                    print(" ".join(args))
                    continue
            elif command.strip().lower().split()[0] == "cat":
                args = command[3::].strip()
                if not args:
                    sys.stdout.write("cat: missing operand\n")
                else:
                    file_paths = []
                    current_arg = ""
                    in_quotes = False
                    quote_char = None
                    
                    for char in args:
                        if char in ["'", '"'] and not in_quotes:
                            in_quotes = True
                            quote_char = char
                        elif char == quote_char and in_quotes:
                            in_quotes = False
                            quote_char = None
                            if current_arg:
                                file_paths.append(current_arg)
                                current_arg = ""
                        elif char == ' ' and not in_quotes:
                            if current_arg:
                                file_paths.append(current_arg)
                                current_arg = ""
                        else:
                            current_arg += char
                    
                    if current_arg:
                        file_paths.append(current_arg)
                    for file_path in file_paths:
                        try:
                            with open(file_path, 'r') as f:
                                content = f.read()
                                print(content, end='')
                        except FileNotFoundError:
                            sys.stdout.write(f"cat: {file_path}: No such file or directory\n")
                        except IsADirectoryError:
                            sys.stdout.write(f"cat: {file_path}: Is a directory\n")
                        except Exception as e:
                            sys.stdout.write(f"cat: {file_path}: {e}\n")

            elif command.strip().lower().split()[0] == "type":
                    args = command.strip().split()[1:]
                    builtins = {"echo", "type", "exit","pwd","cd"}
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
