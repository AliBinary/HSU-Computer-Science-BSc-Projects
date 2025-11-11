from tkinter import *
root = Tk()
root.title("Paint")
root.geometry("500x350")


def paint(event):
    x1, y1 = (event.x-5), (event.y-5)
    x2, y2 = (event.x+5), (event.y+5)
    color = "blue"
    wn.create_oval(x1, y1, x2, y2, fill=color, outline=color)


wn = Canvas(root, width=500, height=400, bg='white')
wn.bind('<B1-Motion>', paint)
wn.pack()
root.mainloop()
