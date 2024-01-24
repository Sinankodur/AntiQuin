from django import forms


class AddressForm(forms.Form):
    class Meta:
        fields = {'address1', 'address2', 'city', 'state', 'pincode'}

    address1 = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'inputAddress',
            'placeholder': 'house no., floor, apartment',
            'autofocus': True,
            'required': True,
        })
    )
    address2 = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'inputAddress2',
            'placeholder': 'area, street, village',
        })
    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'inputCity',
            'required': True,
        })
    )
    state = forms.ChoiceField(
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
            # 'id': 'inputState',
            'required': True,
        })
    )
    pincode = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            # 'id': 'inputZip',
            'required': True,
        })
    )


# class DeliveryContactForm(forms.Form):
#     first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     phone_number = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
