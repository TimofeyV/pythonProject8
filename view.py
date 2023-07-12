def input_num():
    ask = int(input(
        "Выберите действие:\n"
        "1 - Записать нового пользователя\n"
        "2 - Найти контакт\n"
        "3 - Отсортировать  \n"
        "4 - Изменение/Удаление контакта\n"
        "5 - Вывести всех пользователей\n"))
    return ask


def input_name():
    id = input('Введите id: ')
    name = input("Введите имя и фамилию пользователя: ")
    tele = input("Введите номер телефона: ")
    res = id + '_' + name + '_' + tele + "\n"
    return res


def input_char():
    char = input("Введите характеристику: ")
    return char


def input_sort():
    char_sort = int(input("Выберите характеристику по которой будем сортировать:\n"
                          "1 - По id\n"
                          "2 - По имени\n"
                          "3 - По номеру телефона\n"))
    return char_sort


def input_change():
    char_change = int(input("Выберите что вы хотите сделать с контактом:\n"
                            "1 - Удалить\n"
                            "2 - Изменить\n"))
    return char_change
