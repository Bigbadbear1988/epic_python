import math
def functional (x):
    if 0.2 <= x <= 0.9:
        return (math.sin(x))
    else:
        return 1

x = float(input("введите значение x - "))
print (functional (x))
