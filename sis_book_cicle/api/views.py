from rest_framework import viewsets
from book.models import Book
from .serializers import BookSerializer
from rest_framework.pagination import LimitOffsetPagination


class BookViewSet(viewsets.ModelViewSet):
    """Вьюсет для книг."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = LimitOffsetPagination

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)
