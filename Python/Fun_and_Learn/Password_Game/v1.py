import random

password = random.randrange(10)

flag = True
last = "10"
message = "enter a number: "

while (flag):
    ans = input(message)
    if (ans == last):
        message = "This number you said last time.\n say another digit: "
    elif (ans.isdigit() and len(ans) == 1):
        if (int(ans) > password):
            message = "Password is smaller, say another digit: "
        elif (int(ans) < password):
            message = "Password is bigger, say another digit: "
        else:
            message = "yeesss, that's right!"
            flag = False
    else:
        message = "pls enter only one digit number: "
    last = ans

print('\n', message)
print("answer was {} :)".format(password))
