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
