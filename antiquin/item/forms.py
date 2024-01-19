from django import forms

from .models import Product

class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category','name', 'description', 'price', 'image', 'is_sold')