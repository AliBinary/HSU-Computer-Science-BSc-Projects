# Ali Ghanbari
# Student Number: 4001239216

from tkinter import *

MyWindow = Tk()
MyWindow.configure(background="blue")

Window_Width = MyWindow.winfo_reqwidth()
Window_Height = MyWindow.winfo_reqheight()
Right_Position = int(MyWindow.winfo_screenwidth() / 2 - Window_Width/2)
Down_Position = int(MyWindow.winfo_screenheight() / 2 - Window_Height/2)
MyWindow.geometry("+{}+{}".format(Right_Position, Down_Position))

MyWindow.title("Final exam")
MyWindow.geometry('300x400')
MyWindow.resizable(width=False, height=False)


listbox = Listbox(MyWindow, width=31, height=10)
lbl = Label(MyWindow, text="{:10}{:10}{:10}{:10}".format(
    "ID", "Name", "Family", "Average"))

lbl.place(x=50, y=150)
listbox.place(x=50, y=170)

Equation1 = StringVar()
Equation2 = StringVar()
Equation3 = StringVar()
Equation4 = StringVar()


def Clear_Screen():
    Equation1.set("")
    Equation2.set("")
    Equation3.set("")
    Equation4.set("")


File = open("./Students.txt", mode="w")
File.write("\n")
File.close()


def f():
    with open("./Students.txt", mode='a') as File:
        File.write("{:10}".format(MyEntry1.get()))
        File.write("{:10}".format(MyEntry2.get()))
        File.write("{:10}".format(MyEntry3.get()))
        File.write("{:10}\n".format(MyEntry4.get()))

    listbox.insert(1, "{:10}{:10}{:10}{:10}".format(
        MyEntry1.get(), MyEntry2.get(), MyEntry3.get(), MyEntry4.get()))
    Clear_Screen()


MyLabel1 = Label(MyWindow, text="ID:", fg='red', bg='blue')
MyLabel1.place(x=10, y=10)

MyLabel2 = Label(MyWindow, text="Name:", fg='red', bg='blue')
MyLabel2.place(x=10, y=30)

MyLabel3 = Label(MyWindow, text="Family:", fg='red', bg='blue')
MyLabel3.place(x=10, y=50)

MyLabel4 = Label(MyWindow, text="Average:", fg='red', bg='blue')
MyLabel4.place(x=10, y=70)

MyButton = Button(MyWindow, text="add to ListBox & File",
                  fg='white', bg='green', command=lambda: f())
MyButton.place(x=40, y=110)


MyEntry1 = Entry(MyWindow, textvariable=Equation1)
MyEntry1.place(x=70, y=10)

MyEntry2 = Entry(MyWindow, textvariable=Equation2)
MyEntry2.place(x=70, y=30)

MyEntry3 = Entry(MyWindow, textvariable=Equation3)
MyEntry3.place(x=70, y=50)

MyEntry4 = Entry(MyWindow, textvariable=Equation4)
MyEntry4.place(x=70, y=70)

MyWindow.mainloop()
