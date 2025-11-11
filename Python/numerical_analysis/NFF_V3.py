# import essential libraries
import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
from tkinter import messagebox


def clear():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


def hide_frm_Cambox():
    if frm_Cambox.winfo_ismapped():
        frm_Cambox.grid_forget()


def show_frm_Cambox():
    if not frm_Cambox.winfo_ismapped():
        frm_Cambox.grid(row=0, column=0, padx=7, pady=5)
        num_points_label.grid(row=0, column=0)
        num_points_combobox.grid(row=0, column=1, padx=5, pady=5)
        lbl_x1.grid(row=1, column=0, sticky="e")
        ent_x1.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        lbl_h.grid(row=2, column=0, sticky="e")
        ent_h.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        button.grid(row=3, column=1, pady=5)


def hide_frm_Coordinates():
    if frm_Coordinates.winfo_ismapped():
        frm_Coordinates.grid_forget()


def show_frm_Coordinates():
    if not frm_Coordinates.winfo_ismapped():
        frm_Coordinates.grid(row=1, column=0, padx=5, pady=5)


def hide_frm_Buttons():
    if frm_Buttons.winfo_ismapped():
        frm_Buttons.grid_forget()


def show_frm_Buttons():
    if not frm_Buttons.winfo_ismapped():
        frm_Buttons.grid(row=2, column=0, padx=5, pady=5)
        btn_remove.grid(row=0, column=0, sticky="s", padx=10, pady=5)
        btn_add.grid(row=0, column=1, sticky="s", padx=10, pady=6)


def hide_btn_interpolation():
    if btn_interpolation.winfo_ismapped():
        btn_interpolation.grid_forget()


def show_btn_interpolation():
    if not btn_interpolation.winfo_ismapped():
        btn_interpolation.grid(row=1, column=0, columnspan=2, pady=10)


def Try_values():
    flag = 0
    notnum = False
    for i in range(num_points):
        child1 = frm_Coordinates.grid_slaves(row=i, column=1)[0]
        child2 = frm_Coordinates.grid_slaves(row=i, column=3)[0]
        if child2.get():
            try:
                float(child2.get())
                flag += 1
            except ValueError:
                notnum = True
                break

    if notnum:
        messagebox.showerror(
            "Error", "The entered coordinates must be numerical values.")
        return 0
    elif flag < 2:
        messagebox.showerror(
            "Error", "You must enter the coordinates of at least 2 points.")
        return 0
    return 1


def btn_Add():
    if Try_values():
        get_points()
        plot_star(x, y)
        show_btn_interpolation()


def show_points():
    global num_points, X1, H

    for child in frm_Coordinates.winfo_children():
        child.destroy()

    if not (num_points_combobox.get() and ent_h.get() and ent_x1.get()):
        messagebox.showerror("Error", "You must fill in all the blanks")
        return
    try:
        int(num_points_combobox.get())
        float(ent_h.get())
        float(ent_x1.get())
    except ValueError:
        messagebox.showerror(
            "Error", "You must fill in the blanks with numerical values")
        return

    X1 = float(ent_x1.get())
    H = float(ent_h.get())
    num_points = int(num_points_combobox.get())
    if (num_points > 15 or num_points < 2):
        messagebox.showerror(
            "Error", "You can only enter between 2 and 15 points")
        return

    show_frm_Coordinates()
    hide_frm_Cambox()
    show_frm_Buttons()
    hide_btn_interpolation()

    for i in range(num_points):
        y_lbl = tk.Label(frm_Coordinates, text=f"Y{i+1}:")
        y_ent = tk.Entry(frm_Coordinates, width=12)
        y_lbl.grid(row=i, column=2, sticky="w")
        y_ent.grid(row=i, column=3, padx=5, pady=5)

    for i in range(num_points):
        x_lbl = tk.Label(frm_Coordinates, text=f"X{i+1}:")
        x_ent = tk.Entry(frm_Coordinates, width=10)
        x_ent.insert(0, X1 + i * H)
        x_ent.configure(state="readonly")
        x_lbl.grid(row=i, column=0, sticky="w")
        x_ent.grid(row=i, column=1, padx=5, pady=5)


def get_points():
    global x, y, n
    x = []
    y = []
    n = 0

    if Try_values():
        for i in range(num_points):
            child1 = frm_Coordinates.grid_slaves(row=i, column=1)[0]
            child2 = frm_Coordinates.grid_slaves(row=i, column=3)[0]
            if child1.get() and child2.get():
                x.append(float(child1.get()))
                y.append(float(child2.get()))
                n += 1
            elif child1.get():
                x.append(float(child1.get()))
                y.append(0.0)
                n += 1
            elif child2.get():
                x.append(0.0)
                y.append(float(child2.get()))
                n += 1
        clear()
        print("\nX: ", x)
        print("Y: ", y)
        print(f"You have entered the coordinates of {n} points\n")


def btn_Interpolation():
    get_points()
    NFF(x, y, n)
    update_plot(xx, f)


def btn_Remove():
    update_plot([], [])
    plot_star([], [])
    hide_btn_interpolation()
    hide_frm_Buttons()
    hide_frm_Coordinates()
    show_frm_Cambox()


def Enter_Handler(event):
    if frm_Cambox.winfo_ismapped():
        show_points()
    elif btn_interpolation.winfo_ismapped():
        btn_Interpolation()
    elif frm_Buttons.winfo_ismapped():
        btn_Add()


def Del_Handler(event):
    if frm_Buttons.winfo_ismapped():
        btn_Remove()


def NFF(x, y, n):
    global xx, f
    min_value = min(x)
    max_value = max(x)
    z = y
    xx = np.linspace(min_value, max_value, 100)
    f = []
    for ii in range(len(xx)):
        y = z
        p = y[0]
        a = []
        h = x[1] - x[0]
        s0 = (xx[ii] - x[0]) / h
        s = 1
        a.append(y[0])
        for i in range(n-1):
            delf = []
            for j in range(n-1-i):
                delf.append(y[j+1] - y[j])
            s = s*(s0-i)/(i+1)
            p = p+s*delf[0]
            y = delf
            a.append(y[0])
        f.append(p)


def update_plot(a, b):
    line.set_data(a, b)
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw_idle()


def plot_star(a, b):
    stars.set_data(a, b)
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw_idle()


# create window
window = tk.Tk()
window.resizable(width=False, height=False)


# CREATE FIGURE FOR PLOTTING
fig = plt.Figure()
ax = fig.add_subplot(111)
line, = ax.plot([], [], 'b-')
stars, = ax.plot([], [], 'rX')


# create 2 main frames
frm_result = tk.Frame(master=window)
frm_entry = tk.Frame(master=window)

frm_result.grid(row=0, column=0)
frm_entry.grid(row=0, column=1)


# 3 parts of "frm_entry"
frm_Cambox = tk.Frame(frm_entry, relief=tk.RIDGE, borderwidth=5)
frm_Coordinates = tk.Frame(frm_entry)
frm_Buttons = tk.Frame(master=frm_entry, relief=tk.RIDGE,
                       borderwidth=5)

frm_Cambox.grid(row=0, column=0, padx=7, pady=5)
frm_Coordinates.grid(row=1, column=0, padx=5, pady=5)


# build "frm_Cambox" ---> then it builds "frm_Coordinates"
num_points_label = tk.Label(frm_Cambox, text="Number of Points:")
num_points_combobox = ttk.Combobox(
    frm_Cambox, values=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    width=10)
lbl_x1 = tk.Label(frm_Cambox, text="X1=")
ent_x1 = tk.Entry(frm_Cambox, width=10)
lbl_h = tk.Label(frm_Cambox, text="H =")
ent_h = tk.Entry(frm_Cambox, width=10)
button = tk.Button(frm_Cambox, text="Show Points",
                   command=show_points, width=10)

num_points_label.grid(row=0, column=0)
num_points_combobox.grid(row=0, column=1, padx=5, pady=5)
lbl_x1.grid(row=1, column=0, sticky="e")
ent_x1.grid(row=1, column=1, padx=5, pady=5, sticky="w")
lbl_h.grid(row=2, column=0, sticky="e")
ent_h.grid(row=2, column=1, padx=5, pady=5, sticky="w")
button.grid(row=3, column=1, pady=5)


# build "frm_Buttons"
btn_remove = tk.Button(frm_Buttons, text="Remove Points", command=btn_Remove)
btn_add = tk.Button(frm_Buttons, text="Add Points", command=btn_Add)
btn_interpolation = tk.Button(
    frm_Buttons, text="Newton's method of Interpolation",
    command=btn_Interpolation)

btn_remove.grid(row=0, column=0, sticky="s", padx=10, pady=5)
btn_add.grid(row=0, column=1, sticky="s", padx=10, pady=6)

window.bind("<Delete>", Del_Handler)
window.bind("<Return>", Enter_Handler)

canvas = FigureCanvasTkAgg(fig, master=frm_result)
canvas.get_tk_widget().grid()
window.mainloop()
