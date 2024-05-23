import platform
import os

global arch

def check_python_architecture():
    global arch
    architecture = platform.architecture()
    if architecture[0] == '32bit':
        arch = "32BIT"
    elif architecture[0] == '64bit':
        arch = "64BIT"
    else:
        arch = "INVALID"

def main():
    global arch
    print("\033[1;37 •\033[1;36 ×\033[1;37 CHECKING FOR UPDATES")
    os.system("git pull --quiet")
    print(f"\033[1;37 •\033[1;36 ×\033[1;37 {arch} DETECED")
    print("\033[1;37 •\033[1;36×\033[1;37 STARTING JYNX")
    os.system("python jynx.so")

if __name__ == "__main__":
    check_python_architecture()
    main()
