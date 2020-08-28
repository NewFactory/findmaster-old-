from .models import Order
from django.forms import ModelForm, TextInput, EmailInput, Textarea


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["name", "email", "message"]
        widgets = {
            "name": TextInput(attrs={
                'required': True,
                'class': 'form-control',
                'placeholder': 'Your name',
                }),
            "email": EmailInput(attrs={
                'required': True,
                'class': 'form-control',
                'placeholder': 'Email',
                }),
            "message": Textarea(attrs={
                'required': True,
                'class': 'form-control',
                'placeholder': 'Order',
                }),
            }
