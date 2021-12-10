import time
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

while True:
    print('Commands:')
    print('/run - start measuring')
    print('/exit - exit app')
    print()

    input = input('/')

    if input == 'run':
        while True:
            t_end = time.time() + 1

            i = 0


            while time.time() < t_end:
                i = i + 1

            linesPerSec = i
            clearConsole()
            print(linesPerSec, 'lines/second')

    if input == 'exit':
        print('program aborted')

        exit()

    if not input == 'run' or not input == 'exit':
        print('not a command')
        print('start the program and try again')
        exit()