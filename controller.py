from database import *
from view import *


def main():
    while True:
        num = input_num()
        if num == 1:
            res = input_name()
            write_name(res)
            print("Контакт успешно добавлен\n")
        if num == 2:
            char = input_char()
            search_data(char)
        if num == 3:
            char_sort = input_sort()
            if char_sort == 1:
                print("Сортировка по id: ")
                sort_data(1)
            elif char_sort == 2:
                print("Сортировка по имени: ")
                sort_data(2)
            elif char_sort == 3:
                print("Сортировка по номеру телефона: ")
                sort_data(3)
        if num == 4:
            change = input_change()
            print("Найдите контакт, который хотите изменить, по характеристике в списке")
            find = input_char()
            search_data(find)
            print("Для того, чтобы изменить/удалить контакт, необходимо указать его id")
            char = input("id: ")
            if change == 1:
                delete_data(char)
            elif change == 2:
                change_data(char)
            print('Список изменён', end='\n\n')
        if num == 5:
            print("Список: ")
            all_data()


main()
