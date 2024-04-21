import os

# Очистка содержимого экрана
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Главное меню телефонного справочника
def main_menu():
    clear_screen()
    print('Добро пожаловать в телефонный справочник!'
          '\nДоступные команды телефонного справочника:'
          '\n1 - Показать справочник'
          '\n2 - Поиск по справочнику'
          '\n3 - Добавить новую запись'
          '\n4 - Изменить запись'
          '\n5 - Копировать запись'
          '\n6 - Удалить запись'
          '\n0 - Завершение работы со справочником')


# Меню поиска по телефонному справочнику
def search_menu():
    clear_screen()
    print('Параметры поиска:'
          '\n1 - Номер записи'
          '\n2 - Фамилия'
          '\n3 - Имя'
          '\n4 - Отчество'
          '\n5 - Номер телефона'
          '\n0 - Выход в главное меню')


# Меню изменения записи телефонного справочника
def edit_record():
    clear_screen()
    print('Параметры редактирования:'
          '\n1 - Фамилия'
          '\n2 - Имя'
          '\n3 - Отчество'
          '\n4 - Номер телефона'
          '\n0 - Выход в главное меню')


# Вывод на экран телефонного справочника
def show(phone_book):
        print('{:<5} {:<15} {:<15} {:<15} {:<15}'.format(
            '№', 'Фамилия', 'Имя', 'Отчетсво', 'Номер телефона'))
        print('-' * 70)
        for index, data_entry in enumerate(phone_book, start=1):
            print('{:<5} {:<15} {:<15} {:<15} {:<15}'.format(
                index, data_entry[0], data_entry[1], data_entry[2], data_entry[3]))


# Сохранение телефонного справочника в файл
def save_phone_book(phone_book, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for contact in phone_book:
            file.write(', '.join(contact) + '\n')


# Проверка пустой справочник или нет
def empty_book(phone_book):
    if not phone_book:
        input('Справочник пуст!\nНажмите ENTER для продолжения работы со справочником > ')
        return False
    return True


# Поиск по номеру записи
def record_search_row(phone_book, find_user):
    digit = True
    while digit:
        if find_user.isdigit():
            if 0 < int(find_user) <= len(phone_book):
                show([phone_book[int(find_user) - 1]])
            else:
                print('Такой записи в справочнике нет')
            digit = False
        else:
            clear_screen()
            find_user = input('Введите корректный номер строки > ')


# Формирование списка записей по запросу
def record_search_value(phone_book, find_command, find_user):
    temp_book = []
    for contact in phone_book:
        if find_user in contact[int(find_command) - 2]:
            temp_book.append(contact)
    if len(temp_book) > 0:
        show(temp_book)
    else:
        print('Ничего не найдено')


# Добавление записи в телефонный справочник (список в список)
def add_contact(phone_book):
    surname = input('Введите фамилию: ').title()
    name = input('Введите имя: ').title()
    patronymic = input('Введите отчество: ').title()
    phone_number = input('Введите номер телефона: ').title()
    contact = [surname, name, patronymic, phone_number]
    phone_book.append(contact)
    print('Данные успешно добавлены!')


# Внесение изменений в справочник
def edit(phone_book, number_row, parameter_number, new_value):
    if len(phone_book) > 0:
        phone_book[number_row - 1][int(parameter_number) - 1] = new_value
        print('Данные успешно изменены!\n')
        show(phone_book)
    else:
        print('Невозможно внести изменения в пустой справочник!')


# Копирование данных из телефонного справочника
def copy_line(phone_book, number_row):
    if number_row == 0:
        file_path = input('Копирование всего справочника\nПрисвойте имя файлу, в который будет скопирован справочник: ') + '.txt'
        with open(file_path, 'w', encoding='utf-8') as file:
            for entry in phone_book:
                file.write(', '.join(entry) + '\n')
        print(f'Копирование в файл {file_path} завершено!')
    elif 0 < number_row <= len(phone_book):
        entry = phone_book[number_row - 1]
        file_path = input('Копирование выбранной строки\nПрисвойте имя файлу, в который будут скопированы данные из справочника: ') + '.txt'
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(', '.join(entry) + '\n')
        print(f'Копирование в файл {file_path} завершено!')
    input('\nНажмите ENTER для продолжения работы со справочником > ')


# Удаление данных из телефонного справочника
def delete_from_list(phone_book, number_row):
    if number_row == 0:
        del phone_book[:]
        print("Cправочник удален полностью!")
        input('\nНажмите ENTER для продолжения работы со справочником > ')
    elif 0 < number_row <= len(phone_book):
        del phone_book[number_row - 1]
        print(f"Запись №{number_row} удалена")
        input('\nНажмите ENTER для продолжения работы со справочником > ')