print ("Программа для подсчета стоимости билетов в кино.")
print ("")
film = (input("Выбрать фильм: "))
date = (input("Выбрать дату (сегодня, завтра) "))
time = int(input("Выбрать время: "))
quantity = int(input("Указать количество билетов: "))
print ("Вы выбрали фильм: ", film, "День: ", date, "Время: ", time, "Количество билетов: ", quantity)

def first_discount(date):
    if date == "сегодня":
        return 1
    else:
        return 0.95
def second_discount(quantity):
    if quantity >= 20:
        return 0.8
    else:
        return 1
if film == "Пятница":
    if time == 12:
        print ("Результат: ", 250 * quantity * second_discount(quantity) * first_discount(date), "руб.")
    if time == 16:
        print ("Результат: ", 350 * quantity * second_discount(quantity) * first_discount(date), "руб.")
    if time == 20:
        print ("Результат: ", 450 * quantity * second_discount(quantity) * first_discount(date), "руб.")
if film == "Чемпионы":
    if time == 10:
        print ("Результат: ", 250 * quantity * second_discount(quantity) * first_discount(date), "руб.")
    if time == 13:
        print ("Результат: ", 350 * quantity * second_discount(quantity) * first_discount(date), "руб.")
    if time == 16:
        print ("Результат: ", 450 * quantity * second_discount(quantity) * first_discount(date), "руб.")
if film == "Пернатая банда":
    if time == 10:
        print ("Результат: ", 250 * quantity * second_discount(quantity) * first_discount(date), "руб.")
    if time == 14:
        print ("Результат: ", 350 * quantity * second_discount(quantity) * first_discount(date), "руб.")
    if time == 18:
        print ("Результат: ", 450 * quantity * second_discount(quantity) * first_discount(date), "руб.")
else:
    print ("Ошибка ввода.")
    
