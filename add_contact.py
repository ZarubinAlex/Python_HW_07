# Ввод данных в телефонный справочник

import format

def add():

    n = int(input('В какой формат ввести данные (1 или 2): '))

    if 1 <= n <= 2:
        lastName = input('Введите Фамилию: ')
        firstName = input('Введите Имя: ')
        tel = input('Введите Телефон: ')
        comm = input('Введите Описание: ')

        if n == 1:
            format.add_1(lastName, firstName, tel, comm)

        elif n == 2:
            format.add_2(lastName, firstName, tel, comm)

    else: print("выбор неверен")
