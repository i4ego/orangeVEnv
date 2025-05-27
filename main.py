from venv import *

if __name__ == "__main__":
    print("""                                                                                                         
                                                                00      00                                  
      0000    00  0000    000000  000000      000000    0000    00      00    0000    000000    00      00  
    00    00  0000      00    00  00    00  00    00  00000000  00      00  00000000  00    00  00      00  
    00    00  00        00    00  00    00  00    00  00          00  00    00        00    00    00  00    
      0000    00          000000  00    00    000000    000000      00        000000  00    00      00      
                                                  00                                                        
                                              0000                                                          """)

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
                raise SystemExit
            try:
                venv.execute(parsed)
            except Exception as error:
                print_color(31, str(error).replace("()", ""))
        except Exception as error:
            print_color(31, "an error has occurred. error message: " + str(error))