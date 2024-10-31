from django.db import models
from django.contrib.auth import get_user_model 

User = get_user_model() 

# class Author(models.Model):
#     """Модель для Авторов."""
#     def __str__(self):
#         return f'{self.name}'
#     name = models.TextField(
#     )
#     slug = models.SlugField(
#         unique=True
#     )


class Book(models.Model):
    """Модель для Книг."""
    def __str__(self):
        return f'{self.name}'
    name = models.TextField()

    description = models.TextField()    

    availability = models.BooleanField() 

    # author = models.ForeignKey(
    #     Author,
    #     on_delete=models.CASCADE,
    #     related_name='books'
    # )