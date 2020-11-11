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

main - название приложения

Включить приложение в settings.py

INSTALLED_APPS = [
    ...
    'main'
]
    
Добавляем новый урл в urls.py

    urlpatterns = [
        path('', index),
        path('admin/', admin.site.urls),
    ]

Создаем новую функцию в main/views.py

    def index(request):
        return render(request,'index.html')

В settings.py определяем путь к шаблонам.

    TEMPLATES = [
        {
        ....
        'DIRS': [BASE_DIR / 'templates'],

Создаем templates и ложим index.html

    <!DOCTYPE html>
    <html lang="en">


    <head>
        <meta charset="utf-8">
        <title>
            Title
        </title>
    </head>

    <body >

       <h1> Hello </h1>

    </body>

    </html>









