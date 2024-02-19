from django.contrib import admin
from . models import Shelves
from . models import Books, Borrow
# Register your models here.

@admin.register(Books)
class AdminBooks(admin.ModelAdmin):
    list_display = [
        'shelf',
        'name',
        'author',
        'borrowed_on',
        'return_on',
        'category',
        'number_of_pages',
        'written',
        'price'
    ]


class AdminShelver(admin.ModelAdmin):
    list_display = [
        'shelf_number'
    ]

    admin.site.register(Borrow)