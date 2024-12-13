from task.py import (Book, Car, UserProfile)

if __name__ == "__main__":
    # Создание объектов для всех классов
    try:
        book = Book("1984", "George Orwell", 328)
        car = Car("Tesla", "model y", 50.0)
        profile = UserProfile("Sample name", 150, 45)


    except ValueError as e:
        print('Ошибка: неправильные данные')

    # Проверка методов с некорректными аргументами

    try:
        # Попытка создания книги с некорректными кол-вом страниц
        invalid_book = Book("1984", "George Orwell", -100)  # Некорректный аргумент
    except ValueError as e:
        print('Ошибка: неправильные данные')

    try:
        # Попытка создания машины с пустым названием
        invalid_car = Car("", "model y", 50)  # Некорректный аргумент
    except ValueError as e:
        print('Ошибка: неправильные данные')

    try:
        # Попытка создания пользователя с некорректными данными
        invalid_profile = UserProfile("", 150, -5)  # Некорректный аргумент
    except ValueError as e:
        print('Ошибка: неправильные данные')
