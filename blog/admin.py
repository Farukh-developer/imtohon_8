from django.contrib import admin

# Register your models here.

from blog.models import Client, User, Product, Books, Cart

admin.site.register([ Client, User, Product, Books, Cart])