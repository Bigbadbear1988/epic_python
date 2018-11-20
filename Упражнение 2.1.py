def ch_element (x):
    if x == 3:
        return "Li"
    elif x == 25:
        return "Mn"
    elif x == 80:
        return "Hg"
    elif x == 17:
        return "Cl"
    else:
        return "?!"

x = int(input ("Введите атомный номер элемента"))
print (ch_element(x))
