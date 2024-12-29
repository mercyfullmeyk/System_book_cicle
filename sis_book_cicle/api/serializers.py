from rest_framework import serializers
from book.models import Book
import base64
from django.core.files.base import ContentFile


class Base64ImageField(serializers.ImageField):
    """Обработка изображений."""
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]

            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class BookSerializer(serializers.ModelSerializer):
    """Обработка книг."""

    image = Base64ImageField(
        required=False,
        allow_null=True
    )

    class Meta:
        fields = '__all__'
        model = Book



