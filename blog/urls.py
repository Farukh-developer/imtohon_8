from django.urls import path
from .views import BookTypeView, HomeView, LoginView, RegisterView, CartsView, LogoutView, client, DashboardView, DetailView, UsersView, delete_user, UsersEditView

app_name = 'users'


urlpatterns = [
    path('', HomeView.as_view(), name="index"),
    path('book/<int:id>/', BookTypeView.as_view(), name="book"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('client/', client, name='client'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    
    path('carts/', CartsView.as_view(), name='carts'),
    path('register/', RegisterView.as_view(), name='register'),
    path('detail/<int:id>/', DetailView.as_view(), name='detail'),
    path('users/', UsersView.as_view(), name='users'),
    path('delete/<int:id>/', delete_user, name='delete'),
    path('edit/<int:id>/', UsersEditView.as_view(), name='edit'),
    
    
    
    

]