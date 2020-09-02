from django.urls import path
from . import views

app_name = 'performer'
urlpatterns = [
    path('', views.performer, name='performer'),
    path('<int:performer_id>/', views.detail, name='detail'),
    path('<int:performer_id>/leave_review/', views.leave_review, name='leave_review'),

]
