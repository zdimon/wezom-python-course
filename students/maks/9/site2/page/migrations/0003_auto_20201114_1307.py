# Generated by Django 3.1.2 on 2020-11-14 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Catalog',
        ),
    ]
