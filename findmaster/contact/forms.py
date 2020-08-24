from .models import Messages
from django.forms import ModelForm


class ContactForm(ModelForm):
    class Meta:
        model = Messages
        fields = ["name", "email", "message"]
