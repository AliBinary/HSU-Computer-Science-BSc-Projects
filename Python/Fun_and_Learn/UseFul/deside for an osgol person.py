import random
import os


def clrscr():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


clrscr()
L = [2, 3, 5, 7]

if (random.randint(0, 10) in L):
    print("let's play game! ;/")
else:
    print("let's learn programming! XD")
print()
