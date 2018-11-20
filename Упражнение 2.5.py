kod = int(input('Введите код города - ')) 
time = int(input('Введите продолжительность вызова - ')) 
if kod == 343: 
    print('Екатеринбург-код 343, {} руб'.format(time * 15)) 
elif kod == 381: 
    print('Омск-код 381, {} руб'.format(time * 18)) 
elif kod == 473: 
    print('Воронеж-код 473, {} руб'.format(time * 13)) 
elif kod == 485: 
    print('Ярославль-код 485, {} руб'.format(time * 11))
else:
    print ("Такого кода нет в базе")
