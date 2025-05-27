import os, re
import venv
from reader import Reader

def echo(*towrite):
    """Write text to console"""
    print(" ".join(towrite))

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
    print(" ".join(os.listdir()))

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
    os.system(" ".join(command))


def clear(*any):
    """Clear console"""
    print("\033[H\033[J", end="")

def help():
    pass


def file(name):
    """Open .orange file"""
    if re.match(r'.*\.orange$', name):
        if name in os.listdir():
            reader = Reader(venv.OrangeVEnv(venv.commands))
            reader.read(name)
        else:
            raise FileExistsError(f"invalid file! '{name}'")
    else:
        raise NameError(f"not a orangeVEnv file! '{name}' format: <name>.orange")

def exit(*any):
    """Exit from VEnv"""
    raise SystemExit