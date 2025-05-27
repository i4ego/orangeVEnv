import commands
from platform import uname
from getpass import getuser
from os import getcwd

def print_color(color: int|str, text):
    print(f"\033[{color}m" + text + "\033[0m")

def input_command():
    location = f"{getcwd()}\033[32m\033[0m"
    name = f"\033[32m{uname().node}@{getuser()}\033[0m"
    return input(f"\n[{location}]{(len(name)-len(location))*"-"}-\033[38;5;220mOrangeVEnv\033[0m\n{name}>$ ")

class CommandDecodeError(Exception): pass

class OrangeVEnv:
    def __init__(self, cmd_module):

        self.module = cmd_module
        self.commands = list()
        self.module.help = self.help
        for command in dir(cmd_module):
            if str(command)[0] != "_":
                self.commands.append(command)
    def parse(self, command: str):
        if command.split(" ")[0] in self.commands:
            return [command.split(" ")[0], command.split(" ")[1:]]
        else:
            raise CommandDecodeError(f"'{command.split(' ')[0]}' command not found!")
    def execute(self, parsed: list):
        arg_string = str(parsed[1])
        arg = list()
        for symbol in arg_string:
            arg.append(symbol)
        arg[0] = ""
        arg[len(arg)-1] = ""
        arg_string = "".join(arg)
        exec(f"{self.module.__name__}.{parsed[0]}({arg_string})")
    def help(self):
        """Show help"""
        global command_doc
        for cmd in self.commands:
            if cmd == "re" or cmd == "os" or cmd == "venv" or cmd == "Reader": continue
            exec(f"global command_doc; command_doc = {self.module.__name__}.{cmd}.__doc__")
            print_color(34, f"{cmd}{(30 - len(cmd)) * "."}{command_doc}")
        del command_doc