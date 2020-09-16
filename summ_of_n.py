#Сумма элементов от 1 до N (включительно)


def fun(n):
    a = 1
    sums = n
    while n > 1:
        sums = sums + a
        a = a + 1
        n = n - 1
    return sums


print(fun(int(input("Введите N:"))))
