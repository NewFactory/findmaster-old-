from django.urls import path
from . import views


app_name = 'performer'
urlpatterns = [
    path('', views.all_performers, name='all_performers'),
    path('<int:performer_id>/', views.detail, name='detail'),
    path('<int:performer_id>/leave_review/', views.leave_review, name='leave_review'),
    path('group/', views.group.as_view(), name='group'),
    path('group/<int:group_id>/', views.specialization, name='specialization'),
    path('specialization/<int:specialization_id>/', views.performer, name='performer'),
]
