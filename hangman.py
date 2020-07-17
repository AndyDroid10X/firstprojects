import random

words = ['snake', 'tardis', 'dalek', 'gun', 'lalaland']
n = len(words)
word = list(words[random.randint(0, n-1)])
#print(word)
count = len(word)
tab = list('_'*count)
print(tab)
inp = input()[0]
tries = 10

while tries > 0:
    if inp in word:
        print("Right!")
        tab.insert(word.index(inp), inp)
        tab.pop(word.index(inp) + 1)
        print(tab)
        if tab != word:
            inp = input()
    elif inp not in word:
        print("Wrong!")
        tries = tries - 1
        if tries == 0:
            print("Exterminate! *You're dead*")
            break
        print(tab)
        inp = input()
    if tab == word:
        print("Geronimo! You won)")
        break
