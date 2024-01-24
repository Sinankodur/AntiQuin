from django import forms

class AddressForm(forms.Form):
    inputAddress = forms.CharField(
        label='Address line',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'inputAddress',
            'placeholder': 'house no., floor, apartment',
            'autofocus': True,
            'required': True,
        })
    )
    inputAddress2 = forms.CharField(
        label='Address line 2',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'inputAddress2',
            'placeholder': 'area, street, village',
        })
    )
    inputCity = forms.CharField(
        label='City',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'inputCity',
            'required': True,
        })
    )
    inputState = forms.ChoiceField(
        label='State',
        choices=[
            ('', 'Choose...'),
            ('1', 'Andhra Pradesh'),
            ('2', 'Chhattisgarh'),
            ('3', 'Delhi'),
            ('4', 'Goa'),
            ('5', 'Jharkhand'),
            # Add more states as needed
        ],
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'inputState',
            'required': True,
        })
    )
    inputZip = forms.CharField(
        label='PIN Code',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'inputZip',
            'required': True,
        })
    )
