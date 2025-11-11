import os
from time import sleep


# Clearing the Screen
# posix is os name for Linux or mac
# else screen will be cleared for windows
def clear():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


# Printing the os name
print("os name is :", os.name)
print("Screen will now be cleared in 5 Seconds")

# Waiting for 5 seconds to clear the screen
sleep(5)

clear()
