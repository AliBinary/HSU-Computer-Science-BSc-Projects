import csv

# --------------------------------  q1  --------------------
with open("data//qoura_questions.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)

    sum_of_words = 0

    for row in reader:
        words = set()
        for word in row[0].split():
            words.add(word)
        sum_of_words += len(words)


# ----------------------------------  q2  -------------------
with open("data//qoura_questions.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)

    sum_of_raghams = 0
    for row in reader:
        for word in row[0].split():
            for char in word:
                if (char.isnumeric()):
                    sum_of_raghams += 1

with open("data//shereno.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)

    sum_of_digits = 0
    for row in reader:
        for word in row[0].split():
            for char in word:
                if (char.isnumeric()):
                    sum_of_digits += 1

# ----------------------------------  q3  --------------------
file1 = open("data//stopwords.txt", "r", encoding="utf-8")
file2 = open("data//shereno.csv", "r", encoding="utf-8")

stopwords = file1.readlines()

reader = csv.reader(file2)
next(reader)

for i in range(len(stopwords)-1):
    stopwords[i] = stopwords[i][:-1]

sum_of_stopwords_in_poem = 0

for row in reader:
    for word in row[0].split():
        for stopword in stopwords:
            if (word == stopword):
                sum_of_stopwords_in_poem += 1

file1.close()
file2.close()

# -------------------------------- print answers ----------------
# print(sum_of_words)
# print(sum_of_raghams, sum_of_digits)
# print(sum_of_stopwords_in_poem)

file = open("output.txt", "w")
file.truncate()

file.write(str(sum_of_words) + "\n")
file.write("{} {}\n".format(sum_of_raghams, sum_of_digits))
file.write(str(sum_of_stopwords_in_poem))

file.close()
