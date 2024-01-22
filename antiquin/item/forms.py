from django import forms

from .models import Product

INPUT_CLASSES = 'form-control'

class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category','name', 'description', 'price', 'image', 'is_sold')

        widgets = {
            'category' : forms.Select(attrs={
                'class' : INPUT_CLASSES
            }),
            'name' : forms.TextInput(attrs={
                'class' : INPUT_CLASSES
            }),
            'description' : forms.TextInput(attrs={
                'class' : INPUT_CLASSES
            }),
            'price' : forms.NumberInput(attrs={
                'class' : INPUT_CLASSES
            }),
            'image' : forms.FileInput(attrs={
                'class' : INPUT_CLASSES
            }),
            'is_sold' : forms.CheckboxInput(attrs={
                'class' : 'form-check-input ms-2 text-black'
            })

        }