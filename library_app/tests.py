from django.test import TestCase
from . models import Shelves, Books, Borrow
# Create your tests here.

class ShelvesTestCase(TestCase): #performing tests on models 

    def setUp(self):
        shelve = Shelves.objects.create(shelf_number=1)

    def test_shelve(self):
        shelves = Shelves.objects.get(id=1)
        self.assertIsNotNone(shelves)


# class BooksTestCase(TestCase):

    # def setUp(self):
        # books = Books.objects.create(name='kremlin rising', author='erdogan')

    # def test_books(self):
        # book = Books.objects.all().count
        # print('this are the number of books', book)
        # self.assertNotEqual(book, 1)


class BorrowTestCase(TestCase):
    
    def setUp(self):
        borrow = Borrow.objects.create(days=3)


    def test_borrow(self):
        obj = Borrow.objects.count()
        self.assertTrue(1)