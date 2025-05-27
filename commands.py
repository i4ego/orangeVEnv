import os, re


def system(*any):
    """Info about system"""
    uname = os.uname()
    print(f"{uname.sysname} {uname.release} ({uname.release}) on {uname.machine}")
    print(f"{uname.nodename}")

def cd(directory):
    """ChangeDirectory"""
    os.chdir(directory)

def pwd(*any):
    """PrintWorkingDirectory"""
    print(os.getcwd())

def ls(*any):
    """All directories in this directory"""
    dirs = str()
    for dir in os.listdir():
        dirs += dir + " "
    print(dirs)

def pid(*any):
    """PID of this process"""
    print(os.getpid())

def mkdir(name):
    """MaKeDIRectory"""
    os.mkdir(name)

def rmdir(name):
    """ReMoveDIRectory"""
    os.rmdir(name)

def touch(name):
    """Create new file"""
    if re.match(r'.*\..*$', name):
        if name not in os.listdir():
            with open(name, "w"): pass
        else:
            raise FileExistsError(f"file already exits! '{name}'")
    else:
        raise NameError(f"not a file! '{name}'")

def remove(name):
    """Delete file"""
    os.remove(name)

def execute(*command):
    """Run command in Terminal"""
    command_str = str()
    for split in command:
        command_str += split + " "
    os.system(command_str)


def clear(*any):
    """Clear console"""
    if os.uname().sysname == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def help():
    pass

def exit(*any):
    """Exit from VEnv"""
    raise SystemExit