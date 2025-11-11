import math


# 1
print("_"*30, "#1 <rectangular>")
sides = {1: "first", 2: "second", 3: "third"}
valSides = []

for i in range(1, 4):
    x = int(input("enter {} side of triangle: ".format(sides.get(i))))
    valSides.append(x)

be_rectangular = False
for p in valSides:
    for q in valSides:
        if math.hypot(p, q) in valSides:
            be_rectangular = True
            break

if be_rectangular:
    print("yes, it will be a rectangular Triagle!")
else:
    print("No, it will not be a rectangular Triagle!")


# 2
print("_"*30, "#2 <correct gmail>")
gmail = input("enter a gmail: ")
if "@gmail.com" in gmail:
    print("This is a correct gmail!")
else:
    print("This is a false gmail!")


# 3
print("_"*30, "#3 <product>")
List = []
while True:
    Element = input("enter a new Element: ")
    if Element == 'end':
        break
    else:
        List.append(int(Element))

product_numbers = math.prod(List)
print("the product of all the elements is {}".format(product_numbers))


# 4
print("_"*30, "#4 <Fibonacci>")


def Fibonacci(n):
    if n <= 2:
        return 1
    else:
        return(Fibonacci(n-1) + Fibonacci(n-2))


n = int(input("get me n: "))
print("Fibonacci trail to n member: {}".format(Fibonacci(n)))
