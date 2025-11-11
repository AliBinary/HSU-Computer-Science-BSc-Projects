import random
import matplotlib.pyplot as plt

random.seed()

money = []
for i in range(50):
    money.append(10)

for tedad in range(100):
    for people1 in range(50):
        if (money[people1] == 0):
            continue

        people2 = random.randrange(50)
        while (money[people2] == 0):
            people2 = random.randrange(50)
        money[people1] = money[people1] - 1
        money[people2] = money[people2] + 1

plt.bar(range(50), sorted(money, reverse=True))
plt.show()
