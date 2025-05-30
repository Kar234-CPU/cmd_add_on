import sys
import os
import platform
import subprocess
import datetime
import shutil

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def sysinfo():
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"User: {os.getlogin()}")
    print(f"Python: {platform.python_version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")

def listdir(path='.'):
    for f in os.listdir(path):
        print(f)

def search(term, path='.'):
    for root, dirs, files in os.walk(path):
        for name in files:
            if term.lower() in name.lower():
                print(os.path.join(root, name))

def datetime_now():
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

def copy(src, dst):
    try:
        shutil.copy(src, dst)
        print(f"Copied {src} to {dst}")
    except Exception as e:
        print(f"Error: {e}")

def run(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error: {e}")

def help_menu():
    print("cmd_add_on - extra cmd utilities")
    print("clear                - clear screen")
    print("sysinfo              - show system info")
    print("ls [path]            - list directory")
    print("search <term> [path] - search files")
    print("now                  - show date and time")
    print("copy <src> <dst>     - copy file")
    print("run <cmd>            - run shell command")
    print("help                 - show this help")

def main():
    if len(sys.argv) < 2:
        help_menu()
        return
    cmd = sys.argv[1]
    if cmd == 'clear':
        clear()
    elif cmd == 'sysinfo':
        sysinfo()
    elif cmd == 'ls':
        path = sys.argv[2] if len(sys.argv) > 2 else '.'
        listdir(path)
    elif cmd == 'search':
        if len(sys.argv) < 3:
            print("search <term> [path]")
        else:
            term = sys.argv[2]
            path = sys.argv[3] if len(sys.argv) > 3 else '.'
            search(term, path)
    elif cmd == 'now':
        datetime_now()
    elif cmd == 'copy':
        if len(sys.argv) < 4:
            print("copy <src> <dst>")
        else:
            copy(sys.argv[2], sys.argv[3])
    elif cmd == 'run':
        if len(sys.argv) < 3:
            print("run <cmd>")
        else:
            run(' '.join(sys.argv[2:]))
    elif cmd == 'help':
        help_menu()
    else:
        print("Unknown command")
        help_menu()

if __name__ == '__main__':
    main()