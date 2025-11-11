import random
import os


def clear():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


num = ["first", "second", "third", "last", " "]
password = str(random.randrange(10000))
password.zfill(4)

message = "we want to find a password with 4 digits ;)\n\
    Guess the {} digit of the password: ".format(num[0])

for i in range(4):
    flag = True
    last = "10"

    while (flag):
        clear()
        ans = input(message)
        if (ans == last):
            message = "You said {} last time!\n>> say another digit: ".format(
                ans)
        elif (ans.isdigit() and len(ans) == 1):
            if (ans > password[i]):
                message = "The password digit is SMALLER than {}\n>> guess another digit: ".format(
                    ans)
            elif (ans < password[i]):
                message = "The password digit is BIGGER than {}\n>> guess another digit: ".format(
                    ans)
            else:
                message = "yesss that's right{}\n let's find next digit.\n".format(
                    '!'*(i+1)) + "Guess the {} digit of the password: ".format(num[i+1])
                flag = False
        else:
            message = "-- pls enter only a digit number: "
        last = ans

clear()
print("## Great, you guessed the password perfectly")
print("Password was {} :)".format(password))
