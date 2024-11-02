from django.urls import path
from . import views

app_name = 'ice_cream'

urlpatterns = [
    path('', views.index, name='index'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
]
