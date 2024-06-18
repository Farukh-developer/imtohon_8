from django import forms
from blog.models import Product


class CreateBooksForm(forms.ModelForm):
    class Meta:
        model = Product 
        fields = ['name', 'price', 'quantity', 'image', 'book']  
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),

            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'book': forms.Select(attrs={'class': 'form-control'}),
        }