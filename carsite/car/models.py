from django.db import models


class Marka(models.Model):
    title_marka = models.CharField(max_length=16, unique=True, verbose_name='Марка')

    def __str__(self):
        return self.title_marka


class Model(models.Model):
    title_model = models.CharField(max_length=32, unique=True, verbose_name='Модель')
    marka_model = models.ForeignKey(Marka, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title_model} - {self.marka_model}'


class Category(models.Model):
    title_category = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.title_category


class Car(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категории')
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE, verbose_name='Марка')
    model = models.ForeignKey(Model, on_delete=models.CASCADE, verbose_name='Модель')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    year = models.PositiveSmallIntegerField(default=0, verbose_name='Выпуск года')
    mileage = models.PositiveIntegerField(default=0, null=True, blank=True, verbose_name='Пробег')
    city = models.CharField(max_length=30, unique=True, verbose_name='Город')
    country = models.CharField(max_length=30, unique=True, verbose_name='Страна')
    with_photo = models.BooleanField()
    CHOICES_IMAGE = (
        ('Чёрный', 'Чёрный'),
        ('Белый', 'Белый'),
        ('Серий', 'Серий'),
        ('Красный', 'Красный'),
        ('Синий', 'Синий'),
        ('Зелённый', 'Зелённый')
    )
    color = models.CharField(max_length=20, verbose_name='Цвет', choices=CHOICES_IMAGE)
    volume = models.FloatField(default=0.8, verbose_name='Объем')
    CHOICES_BOX = (
        ('Автомат', 'Автомат'),
        ('Механика', 'Механика'),
    )
    box = models.CharField(max_length=10, verbose_name='Коробка', choices=CHOICES_BOX)
    CHOICES_DRIVETRAIN = (
        ('Передний', 'Передний'),
        ('Задний', 'Задний'),
        ('4WD', '4WD')
    )
    drivetrain = models.CharField(max_length=10, choices=CHOICES_DRIVETRAIN)
    CHOICES_ENGINE = (
        ('Бензин', 'Бензин'),
        ('Газ', 'Газ'),
        ('Электро', 'Электро'),
        ('Гибрид', 'Гибрид')
    )
    engine = models.CharField(max_length=10, choices=CHOICES_ENGINE)
    description = models.CharField(null=True, verbose_name='Комментарии')
        CHOICES_RUDDER = (
        ("Слева", "Слева"),
        ("Права", "Права"),
    )
    Rudder = models.CharField(verbose_name='Руль', max_length=12,  choices=CHOICES_RUDDER)

    def __str__(self):
        return f'{self.marka} - {self.model}'
        


class CarPhoto(models.Model):
    image = models.ImageField(upload_to='car_photo/', verbose_name='Изображение')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.image} - {self.car}'
        


class Bet(models.Model):
    car_bet = models.OneToOneField(Car, on_delete=models.CASCADE, verbose_name='Выбрать машины')
    price_bet = models.IntegerField(default=0, verbose_name='Цена ставки')
    total_price = models.IntegerField(default=0, verbose_name='Общая стоимость')
    buy_now = models.IntegerField(default=0, verbose_name='Фикцированная сумма')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return f'{self.buy_now} - {self.car_bet} - {self.total_price}'
