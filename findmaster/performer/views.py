from django.shortcuts import render, redirect
from .models import Performer
#from .forms import PerformerForm


# Create your views here.
def performer (request):
    return render(request,'performer/performer.html')
