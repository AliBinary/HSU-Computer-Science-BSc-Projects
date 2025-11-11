from prettytable import PrettyTable
import math
import os

os.system('cls')

Lnames = []
Lscores = []
Lunits = []
Limpacts = []
i = 1
n = int(input("how many Lesson do you want to enter? "))
print()
while i <= n:
    Lname = input("{}_Enter the name of this lesson: ".format(i))
    Lnames.append(Lname)
    Lscore = float(input("Enter the grade of this lesson: "))
    Lscores.append(Lscore)
    Lunit = int(input("Enter the unit number of this lesson: "))
    Lunits.append(Lunit)
    Limpact = float(Lscore * Lunit)
    Limpacts.append(Limpact)
    i += 1
    print()
Avg = math.fsum(Limpacts) / math.fsum(Lunits)

Workbook = PrettyTable()
Workbook.field_names = ["Lesson name",
                        "Lesson graid",
                        "Lesson unit"]

i -= 2
while i >= 0:
    Workbook.add_row([Lnames[i], Lscores[i], Lunits[i]])
    i -= 1
Workbook.align["Lesson name"] = "l"
Workbook.align["Lesson graid"] = "c"
Workbook.align["Lesson unit"] = "c"
Workbook.sortby = "Lesson graid"

os.system('cls')
print(Workbook)
print("Your average is {}".format(Avg), '\n'*2)
