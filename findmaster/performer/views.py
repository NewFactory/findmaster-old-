from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from .models import Performer
from django.urls import reverse
from django.utils import timezone
#from .forms import PerformerForm

def performer (request):
    performer_list = Performer.objects.order_by('name')[:10]
    return render(request,'performer/performer.html', {'performer_list':performer_list})


def detail(request, performer_id):
    try:
        a=Performer.objects.get(id=performer_id)
    except:
        raise Http404("NO find")

    latest_list_review = a.review_set.order_by('-id')[:10]

    return render(request, 'performer/detail.html', {'performer': a, 'latest_list_review':latest_list_review})


def leave_review(request, performer_id):
    try:
        a=Performer.objects.get(id=performer_id)
    except:
        raise Http404("NO find")
    a.review_set.create(autor=request.POST['name'], email=request.POST['email'], rating=request.POST['rating'], reviews=request.POST['text'], create_date=timezone.now())
    return HttpResponseRedirect(reverse('performer:detail', args=(a.id,)))
