from django.shortcuts import render
from .models import Messages
from .forms import ContactForm


# Create your views here.
def contact(request):
    return render(request,'contact/contact.html')
