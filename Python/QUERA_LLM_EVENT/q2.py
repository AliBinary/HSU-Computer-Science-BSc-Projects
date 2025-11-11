import csv
from itertools import islice
from re import findall
import string
import emoji

puns = string.punctuation

# ----------------------------- q1 -----------------------------
with open('data//qoura_questions.csv', "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)

    num_of_words = set()

    for row in reader:
        for word in row[0].split():
            word = word.lower()
            if (word[0] == 'm' and len(word) > 4):
                if (word[-1] in puns):
                    word = word[:-1]

                if (word[-1] == 't'):
                    num_of_words.add(word)

    num_of_words = len(num_of_words)
    print(num_of_words)

# ----------------------------- q2 -----------------------------
with open('data//qoura_questions.csv', "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)

    num_of_emojies = 0

    for row in reader:
        line = row[0]
        text = emoji.demojize(line)
        text = findall(r'(:[!_\-\w]+:)', text)
        list_emoji = [emoji.emojize(x) for x in text]
        if (len(list_emoji) > 0):
            # print(list_emoji)
            num_of_emojies += 1
    print(num_of_emojies)

# -------------------------------- q3 ---------------------------

with open('data//qoura_questions.csv', "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    num_of_induvigual_words = 0

    words = dict()

    for row in reader:
        for word in row[0].split():
            word = word.lower()

            # while (word[-1] in puns and len(word) > 1):
            #     word = word[:-1]

            # while (word[0] in puns and len(word) > 1):
            #     word = word[1:]

            if (word not in words):
                words[word] = 1
            else:
                words[word] += 1

    # print(words)
    words = {k: v for k, v in sorted(
        words.items(), key=lambda item: item[1], reverse=True)}
    # print(words)
    # print(len(words))

    ans = (list(islice(words, 5)))
    for i in range(len(ans)):
        # pass
        print("{}:{}".format(ans[i], words.get(ans[i])), end=" ")
    print()

# -------------------------------- q4 -----------------------------

    words_repeated_once = [word for word, count in words.items() if count == 1]
    words_repeated_once = len(words_repeated_once)
    print(words_repeated_once)
