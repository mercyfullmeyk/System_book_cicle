from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date
import datetime
User = get_user_model()


class Book(models.Model):
    """Модель для Книг."""
    def __str__(self):
        return f'{self.description[:130]}...'
    name = models.TextField(
        help_text='Название книги'
    )

    description = models.TextField(
        help_text='Описание книги'
    )

    availability = models.BooleanField(
        help_text='В наличии'
    )

    image = models.ImageField(
        upload_to='books/',
        blank=True,
        help_text='Фото книги'
    )
    condition = models.IntegerField(
        default=1,
        help_text='Состояние книги',
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='books'
    )

    coins = models.IntegerField(
        default=0,
        help_text='Стоимость в литкоинах',
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )


class Litcoin(models.Model):
    """Модель для монеты литкоин."""

    coins = models.IntegerField(
        default=10,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )

    author = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )


class Rentsbook(models.Model):
    """Модель для арендованных книг."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='books_author'
    )

    arendator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='books_arendator'
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )

    agree_one = models.BooleanField(default=0)

    agree_two = models.BooleanField(default=0)

    in_rent = models.BooleanField(default=0)

    start_rent = models.DateField(
        default=date.today()
    )

    end_rent = models.DateField(
        default=datetime.date.today() + datetime.timedelta(999999)
    )
