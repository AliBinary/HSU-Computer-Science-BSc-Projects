fibonacci = 1
befor = 1
beffor = 0
sum = 0

# sum of even fibonacci values until 4 million
while (fibonacci <= 4000000):
    if not (fibonacci % 2):
        sum = sum + fibonacci
    fibonacci = befor + beffor
    beffor = befor
    befor = fibonacci

print(sum)
