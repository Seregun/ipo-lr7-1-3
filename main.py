import json

filename = "fish_records.json"

# Загрузка данных из файла или инициализация пустого списка
try:
    with open(filename, "r", encoding="utf-8") as file:  # Указываем кодировку UTF-8
        content = file.read().strip()
        if content:  # Если файл не пуст
            try:
                records = json.loads(content)  # Парсим JSON
            except json.JSONDecodeError:
                print("Ошибка: файл содержит некорректный JSON. Исправьте содержимое файла.")
                records = []  # Инициализация пустого списка
        else:
            records = []  # Инициализация пустого списка
except FileNotFoundError:
    records = []  # Если файл не найден, создаем пустой список

operations_count = 0

while True:
    print("Меню:")
    print("1. Вывести все записи")
    print("2. Вывести запись по полю")
    print("3. Добавить запись")
    print("4. Удалить запись по полю")
    print("5. Выйти из программы")

    choice = input("Выберите пункт: ")

    if choice == "1":  # Вывод всех записей
        if records:
            for record in records:
                print(f"ID: {record['id']}")
                print(f"Название: {record['name']}")
                print(f"Латинское название: {record['latin_name']}")
                print(f"Пресноводная: {record['is_salt_water_fish']}")
                print(f"Количество подвидов: {record['sub_type_count']}")
                print()
        else:
            print("Список записей пуст.")
    elif choice == "2":  # Поиск записи по ID
        search_id = input("Введите ID записи: ")
        record_found = None

        for record in records:
            if record['id'] == search_id:
                record_found = record
                break

        if record_found:
            print(f"Запись по ID {search_id}:")
            print(record_found)
        else:
            print("Запись не найдена.")
    elif choice == "3":  # Добавление записи
        new_record = {
            "id": input("ID: "),
            "name": input("Название: "),
            "latin_name": input("Латинское название: "),
            "is_salt_water_fish": input("Пресноводная (True/False): ").lower() == "true",
            "sub_type_count": int(input("Количество подвидов: "))
        }
        records.append(new_record)

        with open(filename, "w", encoding="utf-8") as file:  # Указываем кодировку UTF-8
            json.dump(records, file, indent=4, ensure_ascii=False)  # ensure_ascii=False для записи в читаемом виде

        print("Запись добавлена.")
        operations_count += 1
    elif choice == "4":  # Удаление записи
        search_id = input("Введите ID записи для удаления: ")
        record_found = None

        for idx, record in enumerate(records):
            if record['id'] == search_id:
                record_found = True
                del records[idx]
                break

        if record_found:
            with open(filename, "w", encoding="utf-8") as file:  # Указываем кодировку UTF-8
                json.dump(records, file, indent=4, ensure_ascii=False)
            print("Запись удалена.")
            operations_count += 1
        else:
            print("Запись не найдена.")
    elif choice == "5":  # Выход
        print(f"Количество операций с записями: {operations_count}")
        break
    else:  # Некорректный ввод
        print("Некорректный ввод. Пожалуйста, выберите пункт из меню.")
