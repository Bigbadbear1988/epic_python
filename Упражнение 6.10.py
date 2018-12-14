tasks = []

def menu_print():
    print("Простой todo:\n    1. Добавить задачу.\n    2. Вывести список задач.\n    3. Выход.")

def main_menu():
    while True:
        menu_print()
        num = int(input("Укажите число: "))
        if num == 1:
            text = input("Сформулируйте задачу: ")
            cat = input("Добавьте категорию к задаче: ")
            date = input("Добавьте время к задаче: ")

            task = ["Задача: ", text, "Категория: ", cat, "Дата: ", date]
            tasks.append(task)
        elif num == 2:
            for task in tasks:
                # print(" ".join(task))
                print(*task)

        elif num == 3:
            break

if __name__ == "__main__":
    main_menu()
            
