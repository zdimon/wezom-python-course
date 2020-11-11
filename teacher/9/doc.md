## Установка 

    pip install Django

Создание проекта

    django-admin startproject myprj

    cd myprj

Создаем базу данных

    ./manage.py migrate

Запускаем сервер

    ./manage.py runserver

Создаем приложение

    ./manage.py startapp main

Включить приложение в settings.py

INSTALLED_APPS = [
    ...
    'main'
]
    






