# Generated by Django 3.1.2 on 2020-11-16 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20201116_2146'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category1',
            new_name='Category',
        ),
        migrations.DeleteModel(
            name='Category2',
        ),
    ]