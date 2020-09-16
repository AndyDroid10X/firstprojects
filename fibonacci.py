#Генератор чисел Фибоначчи
nums = [1, 1]
inp = int(input("Введите количество нужных вам цифр:"))
while inp > 2:
    n = nums[-1] + nums[-2]
    nums.append(n)
    inp = inp - 1
print(nums)
