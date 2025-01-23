from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path(
        '',
        views.index,
        name='index'
    ),
    path(
        'books/<int:book_id>/',
        views.book_detail,
        name='book_detail'
    ),
    path(
        'books/create/',
        views.book_create,
        name='book_create'
    ),
    path(
        'profile/<str:username>/',
        views.profile,
        name='profile'
    ),
    path(
        'books/rent/<int:book_id>/',
        views.book_one_or_two_agree,
        name='book_one_or_two_agree'
    ),
    path(
        'books/<int:book_id>/rent/',
        views.book_rent,
        name='book_rent'
    ),
    path(
        'books/<str:username>/user_rent/',
        views.user_rent,
        name='user_rent'
    ),
    path(
        'books/<str:username>/user_rent/agree/',
        views.book_rent_agree,
        name='book_rent_agree'
    ),

]
