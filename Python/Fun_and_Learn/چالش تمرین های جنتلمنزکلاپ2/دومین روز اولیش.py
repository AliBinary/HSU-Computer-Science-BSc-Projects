import os


def clear():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


clear()
print('>>>   enter the data like this: 1400/11/18   <<<')
data = input("Enter curent data: ")
birth = input("Enter your date of birth: ")
months = {1: 31,
          2: 31,
          3: 31,
          4: 31,
          5: 31,
          6: 31,
          7: 30,
          8: 30,
          9: 30,
          10: 30,
          11: 30,
          12: 29}
Leap = [1, 5, 9, 13, 17, 22, 26, 30]

day = int(data[8:10])
month = int(data[5:7])
year = int(data[:4])
B_year = int(birth[:4])
B_month = int(birth[5:7])
x = B_month
B_day = int(birth[8:10])
B_day = months.get(B_month) - B_day
B_month = 12 - B_month


# def yearIsLeap(Lyear):
#     if Lyear % 33 in Leap:
#         return True
#     else:
#         return False


# def passedDays(m, d):
#     if m <= 6:
#         S = (m-1)*31 + d
#     elif m == 12:
#         S = 336 + d
#     else:
#         S = 186 + (m-7)*30 + d
#     return (int(S))


Sday = day + B_day
Smonth = month + B_month - 1
Syear = year - B_year - 1

if Smonth >= 12:
    Smonth -= 12
    Syear += 1
if Sday >= months.get(x):
    Smonth += 1
    Sday -= months.get(x)

txt = "\nYour age is {} years, {} months and {} days.\n"
print(txt.format(Syear, Smonth, Sday))
