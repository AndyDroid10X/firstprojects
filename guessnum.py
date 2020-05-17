import random

i = random.randint(0, 100)
print ("Угадайте число":)
inp = int(input())
while inp != i:
	if inp < i:
		print ("Меньше. Попробуйте еще раз:")
		inp = int(input())
	elif inp > i:
		print("Больше. Попробуйте еще раз:")
		inp = int(input())
if inp == i:
	print ("Точно!)")
