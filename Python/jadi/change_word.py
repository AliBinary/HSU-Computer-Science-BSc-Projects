import docx

# open the word file
doc = docx.Document('jadi\\word.docx')

# change the file
for para in doc.paragraphs:
    # print(para.text)
    newtxt = ''
    num = 0
    for char in para.text:
        if char.isdigit():
            if num == 0:
                newtxt += char
                num += 1
            else:
                newtxt = newtxt[:-1*num] + char + newtxt[-1*num:]
                num += 1
        else:
            newtxt += char
            num = 0
    para.text = newtxt

# save the file
doc.save('jadi\\new_word.docx')
