from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, User, Litcoin, Rentsbook
from django.core.paginator import Paginator
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from datetime import date
import datetime


def pagic(list_posts, posts_of_page=9): #Функция для пагинации страничек
    '''Функция паджинатор'''
    return Paginator(list_posts, posts_of_page)


def Litic(author): #Функция для работы с Литкоинами
    '''Функция для монет'''
    if Litcoin.objects.filter(author=author.id):
        return Litcoin.objects.filter(author=author.id)[0]
    else:
        return 0


def index(request): #Функция главной страницы сайта
    '''Функция отвечающая за главную страницу'''
    books_list = Book.objects.filter(availability=True)
    title = 'Каталог'
    page_number = request.GET.get('page')
    page_obj = pagic(books_list).get_page(page_number)
    coin = Litic(request.user)

    if request.user.is_authenticated is True:

        if coin == 0:
            coin_lit = Litcoin(author=request.user)
            coin_lit.save()

        rn = Rentsbook.objects.filter(arendator=request.user)

        ob = []
        for r in rn:
            ob.append(r)

        if len(ob) != 0:
            rn = rn[0]
            today = datetime.date.today()
            time_to_td = rn.end_rent - today

            if time_to_td.days <= 0:
                book = rn.book
                rn.delete()
                book.delete()

                context = {
                    'title': title,
                    'books': books_list,
                    'page_obj': page_obj,
                    'coin': coin,
                }

                return render(request, 'books/test_index.html', context)

            resp = (f'У вас осталось {time_to_td.days} '
                    f'дней до конца аренды {rn.book.name}!')

            context = {
                'title': title,
                'books': books_list,
                'page_obj': page_obj,
                'coin': coin,
                'resp': resp
            }

            return render(request, 'books/test_index.html', context)

    context = {
        'title': title,
        'books': books_list,
        'page_obj': page_obj,
        'coin': coin,
    }

    return render(request, 'books/test_index.html', context)


def book_detail(request, book_id): #Функция для детаьлной странички книги
    '''Функция отвечающая за страницу книги'''
    book = Book.objects.filter(id=book_id)
    book = book[0]
    coin = Litic(request.user)

    if request.user.is_authenticated is True:

        rent = Rentsbook.objects.filter(user=request.user, book=book)
        rent_arendator = Rentsbook.objects.filter(
            arendator=request.user,
            book=book
        )

        published_posts = []

        published_posts_are = []

        for post in rent:
            published_posts.append(post)

        for post in rent_arendator:
            published_posts_are.append(post)

        if len(published_posts) != 0:
            context = {
                'rent': rent[0],
                'coin': coin,
            }
            return render(request, 'books/rent_book.html', context)

        if len(published_posts_are) != 0:
            context = {
                'rent': rent_arendator[0],
                'coin': coin,
            }
            return render(request, 'books/rent_book.html', context)

        context = {
            'book': book,
            'coin': coin,
        }
        return render(request, 'books/test_book.html', context)
    
    context = {
        'book': book,
    }
    
    return render(request, 'books/test_book.html', context)


@login_required
def book_create(request): #Функция для добавления книги на сайт
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
def profile(request, username): #Фунция для профиля
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


@login_required
def book_rent(request, book_id): #Функция для запроса аренды книги
    '''Функция отвечающая за аренду книги'''
    book = get_object_or_404(Book, id=book_id)
    title = 'Каталог'
    cost = book.coins
    coin = Litic(request.user)
    rent_arendator = Rentsbook.objects.filter(
        arendator=request.user,
        book=book
    )

    published_posts = []

    for post in rent_arendator:
        published_posts.append(post)

    coin = Litic(request.user)

    context = {
        'title': title,
        'coin': coin,
    }

    if len(published_posts) == 0:
        if book.author == request.user:
            return render(request, 'books/user_false.html', context)
        if request.method == 'POST':
            if coin.coins >= cost:
                rn = Rentsbook(
                    user=book.author,
                    arendator=request.user,
                    book=book
                )
                rn.save()

            return render(request, 'books/rent_recomend.html', context)
    return render(request, 'books/false_rent_recomend.html', context)


@login_required
def book_rent_agree(request, username): #Функция для соглашения на запрос аренды
    '''Функция отвечающая за аренду книги'''
    usersnames = User.objects.filter(username=username)[0]
    rent_user = Rentsbook.objects.filter(user=usersnames, in_rent=0)
    rent_arendator = Rentsbook.objects.filter(arendator=usersnames, in_rent=0)
    coin = Litic(request.user)

    context = {
        'coin': coin,
        'rent_user': rent_user,
        'rent_arendator': rent_arendator
    }

    return render(request, 'books/rent_agree.html', context)


@login_required
def user_rent(request, username): #Функция отвечающая за страницу арендованных человеком книг
    '''Функция отвечающая за страницу арендованных человеком книг'''
    user = User.objects.get(username=username)
    rents = Rentsbook.objects.filter(arendator=user, in_rent=1)
    book_list = [0] * len(rents)
    for i in range(0, len(rents)):
        book_list[i] = rents[i].book

    coin = Litic(user)

    context = {
        'author': user,
        'rents': rents,
        'coin': coin,
    }
    return render(request, 'books/profile_rent.html', context)


def book_one_or_two_agree(request, book_id): #Функция для подтверждения передачи с двух сторон
    '''Функция отвечающая за подтверждение передачи'''
    book = get_object_or_404(Book, id=book_id)
    cost = book.coins
    coin = Litic(request.user)

    if request.method == 'POST' and book.author != request.user:
        if coin.coins >= cost:
            rn = Rentsbook.objects.filter(
                user=book.author,
                arendator=request.user,
                book=book
            )[0]
            rn.agree_two = 1

        if rn.agree_one == 1 and rn.agree_two == 1:
            rn.in_rent = 1
            book.availability = 0
            book.save()
            rn.start_rent = date.today()
            rn.end_rent = datetime.date.today() + datetime.timedelta(30)
            lit = Litcoin.objects.filter(author=request.user)[0]
            lit_author = Litcoin.objects.filter(author=book.author)[0]
            lit.coins = coin.coins - cost
            lit_author.coins += cost
            lit.save()
            lit_author.save()

        rn.save()

    elif request.method == 'POST' and book.author == request.user:
        rn = Rentsbook.objects.filter(user=book.author, book=book)[0]
        rn.agree_one = 1

        if rn.agree_one == 1 and rn.agree_two == 1:
            rn.in_rent = 1
            book.availability = 0
            book.save()
            rn.start_rent = date.today()
            rn.end_rent = datetime.date.today() + datetime.timedelta(30)
            lit = Litcoin.objects.filter(author=request.user)[0]
            lit_author = Litcoin.objects.filter(author=book.author)[0]
            lit.coins = coin.coins - cost
            lit_author.coins += cost
            lit.save()
            lit_author.save()

        rn.save()

    context = {
        'rent': rn,
        'coin': coin,
    }
    return render(request, 'books/rent_book.html', context)
