# Ali ghanbari ___ student number: 4001239216
print("""Bell numbers:
    Enter the number of set members to calculate the number of Partitions!""")
n = int(input('enter n: '))
i = 1
List_now = [1]
List_last = []
while i <= n:
    List_last.clear()
    List_last = List_now.copy()
    List_now.clear()
    List_now.append(List_last[-1])
    while len(List_now) < i:
        sum = List_now[-1] + List_last[len(List_now)-1]
        List_now.append(sum)
        sum = 0
    i += 1

answer = List_now[-1]
print(answer)
