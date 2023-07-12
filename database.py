from view import *


def write_name(name):
    with open('tel.txt', 'a', encoding='UTF-8') as file:
        file.write(name)


def search_data(char, count=1):
    with open('tel.txt', 'r', encoding='UTF-8') as file:
        lst = file.readlines()
        for row in lst:
            if char in row:
                print(count, row, sep="|", end='')
                count += 1
        print(f'Контактов найдено: {count - 1}', end='\n\n')


def all_data():
    with open('tel.txt', 'r', encoding='UTF-8') as file:
        lst = file.readlines()
        for row in lst:
            print(row, end='')
        print('')


def sort_data(char: int):
    with open('tel.txt', 'r', encoding='UTF-8') as file:
        lst = file.readlines()
        if char == 1:
            lst.sort(key=lambda x: int(x.split("_")[0]))
        elif char == 2:
            lst.sort(key=lambda x: x.split("_")[1])
        elif char == 3:
            lst.sort(key=lambda x: int(x.split("_")[2]))
        for row in lst:
            print(row, end='')
        print('')


def delete_data(char, res=[]):
    with open('tel.txt', 'r', encoding='UTF-8') as file:
        lst = file.readlines()
        for row in lst:
            if char not in row:
                res.append(row)
    with open('tel.txt', 'w', encoding='UTF-8') as file:
        for row in res:
            file.write(row)


def change_data(char, res=[]):
    with open('tel.txt', 'r', encoding='UTF-8') as file:
        lst = file.readlines()
        for row in lst:
            if char in row:
                new_row = input_name()
                res.append(new_row)
            else:
                res.append(row)
    with open('tel.txt', 'w', encoding='UTF-8') as file:
        for row in res:
            file.write(row)
