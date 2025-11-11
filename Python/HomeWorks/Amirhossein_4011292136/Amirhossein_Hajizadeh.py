# Amirhossein Hajizadeh
# 4011292136
import random

password = ""

lower = 'abcdefghijklmnopqrstuvwxyz'
password += lower[random.randrange(0, 26)]

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
password += upper[random.randrange(0, 26)]

num = '0123456789'
password += num[random.randrange(0, 10)]

symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
password += symbols[random.randrange(0, 33)]


all = lower + upper + num + symbols
length = 8 - 4
password += "".join(random.sample(all, length))

L = list(password)
random.shuffle(L)
password = "".join(L)


print(password)
