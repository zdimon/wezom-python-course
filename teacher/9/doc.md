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

Создаем templates в папке проекта и ложим index.html

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

Создаем класс модели в файле models.py

    from django.db import models

    class Page(models.Model):
        title = models.CharField(max_length=250)
        content = models.TextField()

https://docs.djangoproject.com/en/3.1/ref/models/fields/#charfield

Создаем файл миграции коммандой 

    ./manage.py makemigrations

Применяем 

    ./manage.py migrate

Создаем команду загрузки данных

в новом каталоге main/management/commands/hello.py

    from django.core.management.base import BaseCommand, CommandError

    class Command(BaseCommand):

        def handle(self, *args, **options):
           print('Hello command!!!')

Запускаем команду 

    ./manage.py hello


Добавляем данные в таблицу 

    from page.models import Page


    class Command(BaseCommand):

        def handle(self, *args, **options):
           print('Hello command!!!')
           Page.objects.all().delete()
           page1 = Page()
           page1.title = 'Index page'
           page1.content = 'content content'
           page1.save()

Выбираем страницу из функци во view

    from page.models import Page

    def index(request):
        page = Page.objects.get(id=7)
        return render(request,'index.html',{"page": page})


Выводим в шаблоне 

    <h1> {{ page.title }} </h1>









