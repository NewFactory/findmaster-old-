from .models import Message
from django.forms import ModelForm, TextInput, EmailInput, Textarea


class ContactForm(ModelForm):
    class Meta:
        model = Message
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
                'placeholder': 'Message',
                }),
            }
