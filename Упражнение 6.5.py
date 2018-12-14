from random import randint

print("Компьютер загадал число.\nУ вас есть три попытки. Удачи!")

num = randint(0, 10)
user = int(input("Попробуйте угадать: "))
pop = 2    
while num != user:
    if num > user:
        print("Попробуйте число больше!")
    else:
        print("Попробуйте число меньше!")
    if pop == 0:
        break
    user = int(input("Попробуйте угадать: "))
    pop -= 1

if num != user:
    print("Game over!")
else:
    print("Победа!")
