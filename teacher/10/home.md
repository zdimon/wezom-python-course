## Домашнее задание.

Создать две модели с категориями и товарами.

Привязать внешним ключом каждый товар к категории.

Сделать админ-интерфейс для этих двух моделей.

Создать команду загрузки тестовых данных для категорий и товаров.

## Пример (категории и товары)

    Мобильные телефоны
        nokia
        samsung
        redmi

    Продукты
        молоко
        хлеб
        яйца
   
и т.д.

Категории имеют одно поле name.

Продукты - 2 поля name и description.

На главной странице сайта вывести список категорий и продуктов.

Каждый продукт содержит ссылку на его подробное описание.

Ссылка может быть следующего вида:

    producl/detail/2

Где 2 - это уникальный идентификатор продукта.

Сделать отдельную страницу с описание продукта где вывести поля name и description.

При этом во вью будет передаваться идентификатор продукта и проводится его поиск из базы данных.

[пример как это делается](https://stackoverflow.com/questions/150505/capturing-url-parameters-in-request-get)

    