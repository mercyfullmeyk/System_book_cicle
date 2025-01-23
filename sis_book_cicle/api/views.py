from rest_framework import viewsets
from book.models import Book
from .serializers import BookSerializer
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import redirect, render



class BookViewSet(viewsets.ModelViewSet):
    """Вьюсет для книг."""
    queryset = Book.objects.filter(availability=True)
    serializer_class = BookSerializer
    pagination_class = LimitOffsetPagination


# def create_svyz(request, username):
#     '''Функция отвечающая за создания связи между телеграмм аккаунтом и аккаунтом на сайте.'''
#     print(request.user.is_authenticated)
#     have = Tg.objects.filter(author=request.user.id)
#     published_posts = []
#     for post in have:
#         if post.is_published:
#             published_posts.append(post)

#     if len(published_posts) == 0:
#         tg = Tg(telegram=username, author=request.user)
#         tg.save()
#     # Tg.objects.get_or_create(author=request.user, telegram=username)

#     return render(request, 'users/logged_out.html')
