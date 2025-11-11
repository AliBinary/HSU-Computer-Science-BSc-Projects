print("Hello, enter students' grades.", end=" ")
print("enter x to complete the expression")

sum = 0
n = int(input("\nEnter the grade of the first student: "))
sum += n
max = n
cnt = 1

while(n != "end"):
    n = input("\nEnter the grade of the next student: ")
    if(n == "end"):
        break
    elif(n.isnumeric()):
        n = int(n)
        sum += n
        cnt += 1
        if(n > max):
            max = n
    else:
        print("\tYour entry is not valid, try again!\n")

print("The highest class score is: {} and the average class score is: {:.2f}".format(
    max, sum / cnt))
