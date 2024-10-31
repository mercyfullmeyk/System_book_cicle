from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/<int:book_id>/', views.book, name='book'),
]