def import_data(file_name):
    phonebook = []
    with open(file_name, 'r') as file:
        for line in file:
            contact = line.strip().split(',')
            phonebook.append(contact)
    return phonebook

def export_data(file_name, phonebook):
    with open(file_name, 'w') as file:
        for contact in phonebook:
            file.write(','.join(contact) + '\n')

def search_contact(phonebook, key):
    for contact in phonebook:
        if key in contact:
            return contact
    return None

def modify_contact(phonebook, key):
    for contact in phonebook:
        if key in contact:
            choice = input("Что вы хотите сделать с контактом (изменить/удалить)? ")
            if choice.lower() == 'изменить':
                new_data = input("Введите новые данные для контакта (через запятую): ")
                new_contact = new_data.split(',')
                contact[:] = new_contact
                print("Контакт успешно изменен.")
            elif choice.lower() == 'удалить':
                phonebook.remove(contact)
                print("Контакт успешно удален.")
            return
    print("Контакт не найден.")

def copy_contact(phonebook, source_index, target_file):
    if source_index >= 0 and source_index < len(phonebook):
        target_contact = phonebook[source_index]
        with open(target_file, 'a') as file:
            file.write(','.join(target_contact) + '\n')
        print("Контакт успешно скопирован.")
    else:
        print("Неверный номер строки. Контакт не скопирован.")

def main():
    file_name = 'phonebook.txt'
    phonebook = import_data(file_name)

    while True:
        print("1. Вывести данные")
        print("2. Сохранить данные")
        print("3. Найти контакт")
        print("4. Изменить или удалить контакт")
        print("5. Скопировать данные в другой файл")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            for contact in phonebook:
                print(contact)
        elif choice == '2':
            export_data(file_name, phonebook)
            print("Данные сохранены в файл.")
        elif choice == '3':
            key = input("Введите имя или фамилию для поиска: ")
            result = search_contact(phonebook, key)
            if result:
                print("Найден контакт: ", result)
            else:
                print("Контакт не найден.")
        elif choice == '4':
            key = input("Введите имя или фамилию для изменения или удаления: ")
            modify_contact(phonebook, key)
        elif choice == '5':
            source_index = int(input("Введите номер строки для копирования: "))
            copy_contact(phonebook, source_index, 'target_phonebook.txt')
        elif choice == '6':
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()