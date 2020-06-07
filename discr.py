# нахождение корней квадратного уравнения

from tkinter import *
import math


def discriminant():
    a = float(enter_a.get())
    b = float(enter_b.get())
    c = float(enter_c.get())

    d = b ** 2 - (4 * a * c)
    if d > 0:
        x1 = (-b + math.sqrt(d)) / 2 * a
        x2 = (-b - math.sqrt(d)) / 2 * a
        label_out.config(text="X1 = " + str(x1) + "\nX2 = " + str(x2))
    elif d == 0:
        x = -b / (2 * a)
        label_out.config(text="У уравнения только один корень: " + str(x))
    elif d < 0:
        label_out.config(text="У уравнения нет решения")


window = Tk()
window.config(width=500, height=500)
window.title("Решение квадратного уравнения")

enter_a = Entry(window, width=5)
label_a = Label(window, text="x^2 + ")
enter_b = Entry(window, width=5)
label_b = Label(window, text="x + ")
enter_c = Entry(window, width=5)
label_out = Label(window)
btn = Button(window, text="Клик!", command=discriminant)


enter_a.place(x=10, y=10)
enter_b.place(x=90, y=10)
label_a.place(x=50, y=10)
enter_c.place(x=157, y=10)
label_b.place(x=130, y=10)
btn.place(x=225, y=50)
label_out.place(x=225, y=90)
window.mainloop()
