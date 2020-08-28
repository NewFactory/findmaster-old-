from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm


# Create your views here.
def order(request):
    error = ''
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Form not correct'


    form = OrderForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request,'order/order.html', context)
