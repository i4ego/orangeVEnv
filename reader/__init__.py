class Reader:
    def __init__(self, venv_obj):
        self.venv = venv_obj
    def read(self, filename: str):
        lines = list
        with open(filename, "r") as file:
            lines = file.readlines()
        for line in lines:
            parsed = self.venv.parse(line)
            self.venv.execute(parsed)