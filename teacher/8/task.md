## Задача 1.

Есть словарь пользователей.

    user1 = {"name": "Kiril", "age": 21}
    user2 = {"name": "Artem", "age": 22}
    user3 = ...

И список - коллекция пользователей.

    collect = [user1,user2,user3....]

Задача запросить у человека имя пользователя.

Затем найти всех пользователей с таким именем или частью имени.

Вывести всех найденных с указанием возраста.

## Задача 2.

Модернизировать программу 1 с использованием функции.

Создать функцию в отдельном файле.

    def search(username):
        ...
        ...
        return list_of_users

Функция принимает имя пользователя, а возвращает массив найденных пользователей.

Использовать ее в основной программе импортировав из внешнего файла.

Например.

    from utils import serach
    name = input('Введите имя')
    print(search(name))

