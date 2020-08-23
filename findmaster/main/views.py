from django.shortcuts import render
from .models import Contact


# Create your views here.
def index(request):
    return render(request,'main/index.html')


def about(request):
    return render(request,'main/about.html')


def contact(request):
    return render(request,'main/contact.html')
