tasks = []

def menu_print():
    print("Простой todo:\n    1. Добавить задачу.\n    2. Вывести список задач.\n    3. Выход.")

def main_menu():
    while True:
        menu_print()
        num = int(input("Укажите число: "))
        if num == 1:
            task = dict()
            task["name"] = input("Сформулируйте задачу: ")
            task["category"] = input("Добавьте категорию к задаче: ")
            task["time"] = input("Добавьте время к задаче: ")
            tasks.append(task)
        elif num == 2:
            from pprint import pprint
            pprint(tasks)

        elif num == 3:
            break

if __name__ == "__main__":
    main_menu()
            
