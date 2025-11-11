def ok(n):
    if not (n % 3 and n % 5):
        return True
    return False


sum = 0
for num in range(1, 1000):
    if ok(num):
        sum += num
print(sum)
