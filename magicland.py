import random
n = random.randint(0, 2)
words = ('hello', 'apple', 'melon')
print (words[n])
inp = input()
for i in range(2):
	while inp != words[n]:
		print("Неправильно!")
		inp = input()
if inp == words[n]:
	print("Правильно!")