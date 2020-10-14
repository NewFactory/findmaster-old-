from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .models import Performer, Group, Specialization
from django.urls import reverse
from django.utils import timezone
#from .forms import PerformerForm
# extra
from django.views import generic

def all_performers (request):
    performer_list = Performer.objects.order_by('name')#[:20]
    return render(request,'performer/all_performers.html', {'performer_list':performer_list})

def detail (request, performer_id):
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
    a.review_set.create(autor=request.POST['name'], email=request.POST['email'], reviews=request.POST['text'], create_date=timezone.now())
    return HttpResponseRedirect(reverse('performer:detail', args=(a.id,)))


class group(generic.ListView):
    model = Group
    template_name = 'performer/group.html'

def specialization(request, group_id):
    try:
        specialization=Specialization.objects.filter(groups_id=group_id)
    except:
        raise Http404("NO findddddddddddddd")
    return render(request, 'performer/specialization.html', {'specialization': specialization})

def performer(request, specialization_id):
    try:
            specializations=Specialization.objects.filter(id=specialization_id)
    except:
        raise Http404("NO frrrrrrrrrrrrrrrrrrr")
    return render(request, 'performer/performer.html', {'specializations':specializations})
