# Generated by Django 3.1.2 on 2020-11-16 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20201116_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='Category1',
        ),
    ]
