from random import randint

stul = ["самовар", "весна", "лето"]
a = randint(0, len(stul)-1)
word = stul[a]
b = randint(0, len(word)-1)
print("Угадайте букву: ", word[:b] + "?" + word[b+1:])
user = input ()
if word [b] == user:
    print ("Победа")
else:
    print ("Поражение")
print ("Слово: ", word)
