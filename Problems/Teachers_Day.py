from os import system
from time import sleep
from keyboard import is_pressed

while 1:
    words = 'HAPPY TEACHER\'S DAY SIR!'.split()
    for word in words:
        for c in word:
            print(c, end="")
            sleep(0.1)
            if is_pressed('esc'):
                print("You've exited the program. Have a nice evening!")
                exit(0)
        print()
    print()







