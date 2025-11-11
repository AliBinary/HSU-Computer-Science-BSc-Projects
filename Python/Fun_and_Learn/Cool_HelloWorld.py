import time

word = input("what do you want to print? ")
word = word.lower()

guess = ""
i = 0

while (True):
    j = 97
    while (chr(j) != word[i]):
        lord = ord(word[i])
        if (lord < 97 or lord > 122):
            j = lord
            break

        print(guess, chr(j), sep='')
        j += 1
        time.sleep(0.1)

    guess += chr(j)
    print(guess)
    i += 1

    if (guess == word):
        print(":)")
        break
