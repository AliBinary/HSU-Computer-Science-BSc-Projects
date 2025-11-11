import random
num = ["first", "second", "third", "last"]

password = str(random.randrange(10000))
password.zfill(4)

for i in range(4):
    flag = True
    last = "10"
    message = "Guess the {} digit of the password: ".format(num[i])

    while (flag):
        ans = input(message)
        if (ans == last):
            message = "\nThis number you said last time.\n   say another digit: "
        elif (ans.isdigit() and len(ans) == 1):
            if (ans > password[i]):
                message = "\nThe password digit is smaller.\n   guess another digit: "
            elif (ans < password[i]):
                message = "\nThe password digit is bigger.\n   guess another digit: "
            else:
                print("\nok!\n let's find next digit.\n")
                flag = False
        else:
            message = "\n   pls enter only a digit number: "
        last = ans

print('\n\n', "yeesss, that's right!")
print("Password was {} :)".format(password))
