from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    USER_ROLE_CHOICES = {
        ("client", "client"),
        ("seller", "seller"),
        ("admin", "admin"),
    }
    image = models.ImageField(upload_to='profile_pics/', null=True, blank=True, default="profile_pics/default.jpeg")
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    user_role = models.CharField(max_length=10, choices=USER_ROLE_CHOICES, default="client")

class Books(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"
    
class Product(models.Model):
    name=models.CharField(max_length=150)
    price=models.IntegerField()
    quantity = models.PositiveIntegerField()
    image=models.ImageField(upload_to='shop_picture', null=True, blank=True)
    book=models.ForeignKey(Books, on_delete=models.CASCADE, related_name='book')
    def __str__(self):
        return f"{self.name}"
    
class Cart(models.Model):
    product=models.OneToOneField(Product, on_delete=models.CASCADE, related_name='cart')
    quantity=models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.product.name}"
    
    
    @property
    def total_price(self):
        return self.product * self.quantity

    

    
    
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    
    
    def __str__(self):
        return f"{self.user.username}"
    

   
    