def even (x):
    if x%2 == 0:
        return "even"
    else:
        return "odd"
x = int(input("Введите число для проверки - "))
print (even(x))
