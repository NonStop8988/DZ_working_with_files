from data_create import *

def phone_book():
    phone_book = []
    isStop = True
    phone_book_filename = 'phone_book.txt'

    while isStop:

        main_menu()
        command = input("Введите желаемую команду >>> ")

        if command == "0":
            print("Всего хорошего!")
            isStop = False

        elif command == '1':
            if len(phone_book) > 0:
                show(phone_book)
            else:
                print('Телефонная книга пуста!')
            input('\nНажмите ENTER для продолжения работы со справочником > ')

        elif command == '2':
            stop_comand = empty_book(phone_book)
            while stop_comand:
                search_menu()
                find_command = input("Введите желаемую команду >> ")
                if find_command == '1':
                    clear_screen()
                    find_user = input('Введите поисковые данные > ')
                    record_search_row(phone_book, find_user)
                    input('\nНажмите ENTER для продолжения работы с поиском > ')
                elif find_command in ['2','3','4','5']:
                    find_user = input('Введите поисковые данные > ').title()
                    record_search_value(phone_book, find_command, find_user)
                    input('\nНажмите ENTER для продолжения работы с поиском > ')
                elif find_command == '0':
                    stop_comand = False

        elif command == '3':
            add_contact(phone_book)
            save_phone_book(phone_book, phone_book_filename)
            input('\nНажмите ENTER для продолжения работы со справочником > ')

        elif command == '4':
            stop_comand = empty_book(phone_book)
            while stop_comand:
                clear_screen()
                show(phone_book)
                number_row = input('\nУкажите номер строки для редактирования данных или введите 0 для выхода в главное меню > ')
                if number_row.isdigit():
                    number_row = int(number_row)
                    if number_row <= 0 or number_row > len(phone_book):
                        if number_row == 0:
                            stop_comand = False
                    else:
                        parameter_number = 0
                        while parameter_number not in ['0','1','2','3','4']:
                            edit_record()
                            parameter_number = input('Укажите параметр редактирования >> ')
                        if parameter_number == '0':
                            stop_comand = False
                        else:
                            new_value = input('Введите новое значение > ').title()
                            edit(phone_book, number_row, parameter_number, new_value)
                            save_phone_book(phone_book, phone_book_filename)
                            stop_comand = False
                            input('\nНажмите ENTER для продолжения работы со справочником > ')

        elif command == '5':
            stop_comand = empty_book(phone_book)
            while stop_comand:
                print()
                clear_screen()
                show(phone_book)
                number_row = input('\nУкажите номер строки, которую вы хотите скопировать или введите 0 для копирования всего справочника\nДля возвращения в главное меню нажмите ENTER > ')
                if not number_row.strip():
                    stop_comand = False
                elif number_row.isdigit():
                    number_row = int(number_row)
                    if 0 <= number_row <= len(phone_book):
                        copy_line(phone_book, number_row)
                        stop_comand = False


        elif command == '6':
            stop_comand = empty_book(phone_book)
            while stop_comand:
                print()
                clear_screen()
                show(phone_book)
                number_row = input('\nУкажите номер строки, которую вы хотите удалить или введите 0 для удаления всего справочника\nДля возвращения в главное меню нажмите ENTER > ')
                if not number_row.strip():
                    stop_comand = False
                elif number_row.isdigit():
                    number_row = int(number_row)
                    if 0 <= number_row <= len(phone_book):
                        delete_from_list(phone_book, number_row)
                        stop_comand = False