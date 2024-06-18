from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Product
from blog.permission import SellerRequiredMixin
from django.views import View
from .forms import CreateBooksForm
# Create your views here.

class SellerView(SellerRequiredMixin ,View):
    def get(self, request):
        return render(request, 'user/dashboard.html') 
    
    
class BooksHomeView(View):
    def get(self, request):
        product=Product.objects.all()
        return render(request, 'user/index.html', context={"product":product})
    
    
class CreateBookView(SellerRequiredMixin, View):
    def get(self, request):
        form = CreateBooksForm()
        return render(request, 'seller/creat.html', context={"form":form})
    
    def post(self, request):
        form = CreateBooksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('seller:book')
        return render(request, 'seller/creat.html', {'form': form}) 
    
    
    
    
    

    
    
