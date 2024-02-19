from django.db import models
from . managers import BookManager
# Create your models here.
class Shelves(models.Model):
    shelf_number = models.IntegerField(null=True, unique=False)

class Books(models.Model):
    category_choices = (
        ('frt', 'fairy tale'),
        ('fts', 'fantasy'),
        ('crm,', 'crime'),
        ('hrr', 'horror'),
        ('fcn', 'fiction')
    )
    shelf = models.IntegerField(null=True)
    name = models.CharField(max_length=30, null=True)
    author = models.CharField(max_length=30, null=True)
    borrowed_on = models.DateTimeField(auto_now_add=True, null=True)
    return_on = models.DateTimeField(auto_now=True, null=True)
    category = models.CharField(max_length=10, choices=category_choices, null=True)
    number_of_pages = models.IntegerField(null=True)
    written = models.DateField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)


    def __str__(self):
        return self.name
    
    class Meta:
        
        ordering = [
            '-name'
        ]

    #custom permissions for the staff who will be adding books

    permissions = [
        ('add_book', 'users can add books') 
    ]

    # custom model manager for the books
    book_manager = BookManager()

class Borrow(models.Model):
    days = models.IntegerField()

    # def __str__(self):
        # return self.days

    # function to calculate the fee to be charged 
    def penal_func(self):
        return self.days * 500