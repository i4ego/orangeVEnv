from venv import *

if __name__ == "__main__":
    venv = OrangeVEnv(commands)
    while 1:
        try:
            parsed = list()
            try:
                inp = input_command()
                parsed = venv.parse(inp)
            except CommandDecodeError as error:
                print_color(31, str(error))
                continue
            except KeyboardInterrupt:
                sys.stdout.flush()
                raise SystemExit
            try:
                venv.execute(parsed)
            except Exception as error:
                print_color(31, str(error).replace("()", ""))
        except Exception as error:
            print_color(31, "an error has occurred. error message: " + str(error))