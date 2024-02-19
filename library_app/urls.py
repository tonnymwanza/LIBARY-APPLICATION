from django.urls import path
from . views import BorrowView
from library_app import views
# create your url patterns here

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    path('search', views.search, name='search'),
    path('book_details/<int:pk>/', views.book_details, name='book_details'),
    path('borrow_func/<int:pk>/', views.borrow_func, name='borrow_func'),
    path('calculate', BorrowView.as_view(), name='calculate'),
    path('calculate_func', views.calculate_func, name='calculate_func'),
]