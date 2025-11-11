def sums_nums(num):
    sum = 0
    for i in range(5):
        sum += int(num[i])
    return sum


for ramz in range(0, 100000):
    num = str(ramz).zfill(5)

    if (int(num[4]) + int(num[2]) == 14) and \
        (int(num[0]) == int(num[1])*2 - 1) and \
        (int(num[3]) == int(num[1]) + 1) and \
        (int(num[1]) + int(num[2]) == 10) and \
            sums_nums(num) == 30:
        print(num)
