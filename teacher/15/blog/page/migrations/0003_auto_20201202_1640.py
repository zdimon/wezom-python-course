# Generated by Django 3.1.4 on 2020-12-02 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_page_alias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='alias',
            field=models.SlugField(),
        ),
    ]
