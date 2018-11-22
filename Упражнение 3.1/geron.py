def geron(a, b, c): 
    ''' Вычисляет площадь треугольника по формуле Герона:
    >>> geron(3, 4, 5)
    6.0
    
    >>> geron(7, 8, 9)
    26.83
    '''
    
    p = (a+b+c)/2
    print (p)
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    return round(s, 2)
  
if __name__ == "__main__":
    import doctest
    doctest.testmod()
