from django.http import HttpResponse    
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q, Sum
from . forms import BooksForm
from . forms import BorrowForm
from . models import Books
from . models import Borrow
from django.views import View
from django.contrib import messages
# Create your views here.
class HomePageView(View): #usng a class-based view to render the homepage
    
    BooksForm
    Books

    def get(self, request):
        form = BooksForm(request.GET)
        all_books = Books.book_manager.all()[0:5]
        context= {
            'form': form,
            'all_books': all_books
        }
        return render(request, 'home.html', context)

    def post(self, request):
        form = BooksForm(request.POST)
        if form.is_valid():
            obj = Books.book_manager.create(
                shelf = form.cleaned_data['shelf'],
                name = form.cleaned_data['name'],
                author = form.cleaned_data['author'],
                category = form.cleaned_data['category'],
                number_of_pages = form.cleaned_data['number_of_pages'],
                # written = form.cleaned_data['written'],
                price = form.cleaned_data['price']
            )
            messages.success(request, 'the book has been added')
            form = BooksForm()
        else:
            messages.error(request, 'problem encountered while adding book')
            form = BooksForm()

        context = {
            'form': form
        }
        return render(request, 'home.html', context)


def search(request, *args, **kwargs):
    query = None
    q =  request.GET['q']
    books = Books.book_manager.filter(
        Q(name__icontains=q)|
        Q(author__icontains=q)
    )
    context = {
        'books': books
    }
    return render(request, 'search.html', context)


def book_details(request, pk):
    books = Books.book_manager.get(id=pk)
    context = {
        'books': books
    }
    return render(request, 'book_details.html', context)


@login_required(login_url='login')
def borrow_func(request, pk):
    form = BorrowForm()
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            days = form.cleaned_data['days'],
            form.save()
            form = BorrowForm()
            # penal = days * 500
        else:
            form = BorrowForm()
    books = Books.book_manager.get(id=pk)
    context = {
        'books': books,
        'form': form
    }
    return render(request, 'borrow.html', context)


class BorrowView(View):
    
    def get(self, request, *args, **kwargs):
        form = BorrowForm(request.GET)
        borrow = Borrow.objects.all()
        if form.is_valid():
            form.save()
            form = BorrowForm()
        else:
            form = BorrowForm()
        print(request.GET)
        context = {
            'form': form,
            'borrow': borrow 
        }
        return render(request, 'borrow.html', context)

    def post(self, request, *args, **kwargs):
        form = BorrowForm(request.POST)
        borrow = Borrow.objects.all()
        if form.is_valid():
            form.save()
            form = BorrowForm()
        else:
            form = BorrowForm()
        context = {
            'form': form,
            'borrow': borrow 
        }
        return render(request, 'borrow.html', context)

def calculate_func(request):
    if request.method == 'GET':
        days = request.GET['days']
        penalty = int(days)  * 500
    context = {
        'penalty':penalty
        }
    return render(request, 'borrow.html', context)

