# Generated by Django 5.0.3 on 2024-04-09 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0009_alter_bet_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(choices=[('Чёрный', 'Чёрный'), ('Белый', 'Белый'), ('Серий', 'Серий'), ('Красный', 'Красный'), ('Синий', 'Синий'), ('Зелённый', 'Зелённый')], max_length=20, verbose_name='Цвет'),
        ),
    ]
