print('for example: 1400/11/04')
data = input("enter data: ")

week = {0: "sunday",
        1: "monday",
        2: "tuesday",
        3: "wednesday",
        4: "thursday",
        5: "friday",
        6: "saturday"}

day = int(data[8:10])
month = int(data[5:7])
year = int(data[:4])


def passedDays():
    if month <= 6:
        S = (month-1)*31 + day
    elif month == 12:
        S = 336 + day
    else:
        S = 186 + (month-7)*30 + day
    return(int(S))


Leap = [1, 5, 9, 13, 17, 22, 26, 30]


def yearIsLeap(Syear):
    if Syear % 33 in Leap:
        return True
    else:
        return False


Sweek, Syear = 5, 1

while Syear < year:
    Syear += 1
    if not yearIsLeap(Syear):
        Sweek += 1
    else:
        Sweek += 2

Sweek = (passedDays()-1 + Sweek) % 7
print(week.get(Sweek))
