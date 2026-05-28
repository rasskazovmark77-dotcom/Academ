todo_list = []  # пустой список
grades = [5, 4, 5, 3]  # список чисел
names = ["Анна", "Марк", "Оля"]  # список строк

todo_list.append("Купить хлеб")    #Добавить дело в конец

del todo_list[0]      #Удалить дело по индексу

for item in todo_list: print(item)      #Посмотреть все дела

#if not todo_list:     #Проверить, пуст ли список