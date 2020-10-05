from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from .models import Performer
from .models import Group
from django.urls import reverse
from django.utils import timezone
#from .forms import PerformerForm


def group (request):
    group_list = Group.objects.order_by('name')
    return render(request,'performer/group.html', {'group_list':group_list})

def performer (request):
    performer_list = Performer.objects.order_by('name')[:20]
    return render(request,'performer/performer.html', {'performer_list':performer_list})


def detail(request, performer_id):
    try:
        a=Performer.objects.get(id=performer_id)
    except:
        raise Http404("NO find")
    latest_list_review = a.review_set.order_by('-id')[:10]
    return render(request, 'performer/detail.html', {'performer': a, 'latest_list_review':latest_list_review})


# def group_detail(request, performer_id):
#     try:
#         b=Group.objects.get(id=group_id)
#     except:
#         raise Http404("NO find")
#     return render(request, 'performer/group_detail.html', {'group': b})


def leave_review(request, performer_id):
    try:
        a=Performer.objects.get(id=performer_id)
    except:
        raise Http404("NO find")
    a.review_set.create(autor=request.POST['name'], email=request.POST['email'], reviews=request.POST['text'], create_date=timezone.now())
    return HttpResponseRedirect(reverse('performer:detail', args=(a.id,)))
