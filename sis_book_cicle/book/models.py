from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
User = get_user_model()


class Book(models.Model):
    """Модель для Книг."""
    def __str__(self):
        return f'{self.description[:130]}...'
    name = models.TextField()

    description = models.TextField()    

    availability = models.BooleanField()

    image = models.ImageField(
        upload_to='books/',
        blank=True
    )
    condition = models.IntegerField(
        default=1,
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


class Litcoin(models.Model):
    """Модель для монеты литкоин."""

    coins = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )

    author = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
