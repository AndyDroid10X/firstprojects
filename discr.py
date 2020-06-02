# нахождение корней квадратного уравнения
import math


def discriminant(a, b, c):
    d = b ** 2 - (4 * a * c)
    if d > 0:
        x1 = (-b + math.sqrt(d)) / 2 * a
        x2 = (-b - math.sqrt(d)) / 2 * a
        print("X1 = " + str(x1) + "\nX2 = " + str(x2))
    elif d == 0:
        x = -b / (2 * a)
        print("У уравнения только один корень: " + str(x))
    elif d < 0:
        print("У уравнения нет решения")


discriminant(float(input("Введите A:")), float(input("Введите B:")), float(input("Введите C:")))
