from django.shortcuts import render, redirect
from .models import Book, User, Litcoin
from django.core.paginator import Paginator
from .forms import BookForm
from django.contrib.auth.decorators import login_required


def pagic(list_posts, posts_of_page=9):
    '''Функция паджинатор'''
    return Paginator(list_posts, posts_of_page)


def Litic(author):
    '''Функция для монет'''
    return Litcoin.objects.filter(author=author)[0]



def index(request):
    '''Функция отвечающая за главную страницу'''
    books_list = Book.objects.all()
    title = 'Каталог'
    page_number = request.GET.get('page')
    page_obj = pagic(books_list).get_page(page_number)
    coin = Litic(request.user)
    context = {
        'title': title,
        'books': books_list,
        'page_obj': page_obj,
        'coin': coin,
    }

    return render(request, 'books/test_index.html', context)


def book_detail(request, book_id):
    '''Функция отвечающая за страницу книги'''
    book = Book.objects.filter(id=book_id)
    book = book[0]
    coin = Litic(request.user)
    context = {
        'book': book,
        'coin': coin,
    }
    return render(request, 'books/test_book.html', context)


@login_required
def book_create(request):
    '''Функция отвечающая за создание поста'''
    coin = Litic(request.user)
    form = BookForm(request.POST or None,
                    files=request.FILES or None,)

    if form.is_valid():

        book = form.save(commit=None)
        book.author = request.user
        book.availability = True
        book.save()

        return redirect('book:index')

    context = {
        'form': form,
        'coin': coin,
    }
    return render(request, 'books/create_book.html', context)


@login_required
def profile(request, username):
    '''Функция отвечающая за страницу профиля'''
    author = User.objects.get(username=username)
    book_list = Book.objects.filter(author=author)
    coin = Litic(author)

    context = {
        'author': author,
        'books': book_list,
        'coin': coin,
    }
    return render(request, 'books/profile.html', context)