def functional (x):
    if -2.4 <= x <= 5.7:
        return x**2
    else:
        return 4

x = int(input("введите значение x - "))
print (functional (x))
