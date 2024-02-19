from django.db.models import Manager
# creating a custom manager for Book model
class BookManager(Manager):
    def get_books(self):
        return self.get_queryset.all()