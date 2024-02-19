from django import forms
from . models import Books
from . models import Borrow
import random
from django.core.exceptions import ValidationError

class BooksForm(forms.Form):
    category_choices = (
        ('frt', 'fairy tale'),
        ('fts', 'fantasy'),
        ('crm,', 'crime'),
        ('hrr', 'horror'),
        ('fcn', 'fiction')
    )
    shelf = forms.IntegerField()
    name = forms.CharField(max_length=30)
    author = forms.CharField(max_length=30)
    category = forms.CharField(widget=forms.RadioSelect(choices=category_choices))
    number_of_pages = forms.IntegerField()
    # written = forms.DateTimeField()
    price = forms.DecimalField()
    

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = [
            'days'
        ]