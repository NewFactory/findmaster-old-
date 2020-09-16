from django.shortcuts import render, redirect
from .models import Message
from .forms import ContactForm


# Create your views here.
def contact(request):
    error = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:index')
        else:
            error = 'Form not correct'


    form = ContactForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request,'contact/contact.html', context)
