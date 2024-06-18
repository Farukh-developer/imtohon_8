from django.urls import path
from .views import SellerView, BooksHomeView, CreateBookView

app_name='seller'


urlpatterns = [
    path('seller/', SellerView.as_view(), name='seller'),
    path('book/', BooksHomeView.as_view(), name='book'),
    path('create/', CreateBookView.as_view(), name='create'),
    
    
]
