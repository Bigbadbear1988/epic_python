def f(s, n):
    if len(s) > n:
        return s.upper()
    else:
        return s

s = (input('Введите текст - ')) 
n = int(input('Введите число - '))
result = f(s, n)
print(result)
