from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import LoginForm, RegisterForm, UsersEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User, Product, Client, Books, Cart
from .permission import AdminRequiredMixin, ClientRequiredMixin, SellerRequiredMixin
from django.db.models import Q

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "user/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.user_role == 'admin':
                    return redirect('users:dashboard')
                elif user.user_role == 'client':  
                    return redirect("users:index")
                elif user.user_role == 'seller':
                    return redirect("seller:seller")

        form = LoginForm()
        return render(request, "user/login.html", {"form": form})


class DashboardView(AdminRequiredMixin, View):
    def get(self, request):
        return render(request, 'user/dashboard.html')
    
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('users:index')
    

class UsersView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'user/users.html', context={"users":users})
      


class CartDetailView(View):
    def get(self, request):
        books = Books.objects.all()
        cart=Cart.objects.all()
        count = Cart.objects.count()
        product = Product.objects.all()
        return render(request, 'user/carts.html', {'books': books, "cart":cart , 'count':count, 'product': product})

class RegisterView(ClientRequiredMixin,View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'user/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            if user.user_role == 'seller':
                new_seller=User()
                new_seller.user_id = user
                new_seller.save()
            elif user.user_role == 'client':
                new_client=Client()
                new_client.user=user
                new_client.save()
                

            return redirect('/')

        form = RegisterForm()
        return render(request, 'user/register.html', {'form': form})
    
    

   
   
 
class HomeView(ClientRequiredMixin,View):
    def get(self, request):
        book=Books.objects.all()
        product=Product.objects.all()
        count=Cart.objects.count()
        return render(request, 'user/index.html', context={"book":book, "product":product, "count":count}) 
    

class BookTypeView(ClientRequiredMixin, View):
    def get(self, request, id):
        book=get_object_or_404(Books, id=id)
        product=book.book.all()
        book=Books.objects.all()
        return render(request, 'user/index.html', context={"product":product, "book":book})
    
class CartsView(ClientRequiredMixin,View):
    def get(self, request):
        product = Cart.objects.all()
        return render(request, 'user/carts.html',{'product':product})   
    
    
def client(request):
    client=Client.objects.all()
    return render(request, 'user/clients.html', context={"client":client})
    
    
    
             
class DetailView(View):
    def get(self, request, id):
        products=get_object_or_404(Product, id=id)
        cart=Cart.objects.count()
        return render(request, 'user/detail.html', context={"products":products, "cart":cart})
        
    def post(self, request, id):
        products=get_object_or_404(Product, id=id)
        quantity=int(request.POST['cart'])
        if Cart.objects.filter(product=products).exclude():
            cart=Cart.objects.filter(product=products).first()
            cart.quantity += quantity
            cart.save()
        else:    
            cart=Cart()
            cart.product=products
            cart.quantity=quantity
            cart.save()
        return redirect('users:carts')   
            

class UsersEditView(AdminRequiredMixin, View):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        form = UsersEditForm(instance=user)
        return render(request, 'user/edit_users.html', context={"form": form})
    
    def post(self, request, id):
        user = get_object_or_404(User, id=id)
        form = UsersEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()  
            return redirect('users:users')
        return render(request, 'user/edit_users.html', context={"form": form})

            
        
        
        
        

        
def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('/users')
    