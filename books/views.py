from django.shortcuts import render
from books.models import Book
from datetime import datetime, date, time

def books_view(request, pub_date=None):
    template = 'books/books_list.html'
    books = Book.objects.all()
    book_list = []
    date_list = []
    for book in books:
        public_date = book.pub_date.strftime('%Y-%m-%d')
        book_list.append({'name': book.name, 'author': book.author, 'pub_date': public_date})
        date_list.append(public_date)
    date_list.sort()
    date_list = list(set(date_list))
    prev_page = None
    next_page = None

    if pub_date:
        book_list = []
        selected_books = Book.objects.filter(pub_date=pub_date)
        for book in selected_books:
            public_date = book.pub_date.strftime('%Y-%m-%d')
            book_list.append({'name': book.name, 'author': book.author, 'pub_date': public_date})
        index = date_list.index(pub_date.strftime('%Y-%m-%d'))
        if index != 0:
            prev_page = date_list[index-1]
        if index != len(date_list)-1:
            next_page = date_list[index+1]

    

    context = {
        'books': book_list,
        'pub_date': pub_date,
        'prev_page': prev_page,
		'next_page': next_page,
    }
    return render(request, template, context)
