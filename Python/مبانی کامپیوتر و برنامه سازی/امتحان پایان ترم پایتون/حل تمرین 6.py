List = []
lenList = int(input("What is the degree of this polynomial?  "))
print("Enter polynomial coefficients in order")
for p in range(0, lenList):
    elm = input()
    List.append(elm)
print(List)

answer = ''
degree = 0
for i in List:
    if List.index(i) == 0:
        answer = answer + f"{i}"
    else:
        answer = answer + f" + {i}X^{degree}"
    degree += 1
print(answer)
