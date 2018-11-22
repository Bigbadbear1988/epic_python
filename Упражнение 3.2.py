import random
num = random.randint (1,4)
x = int(input("введите число - "))
if num == x:
    print ("Победа")
elif num > x:
    print (">")
else:
    print ("<")

