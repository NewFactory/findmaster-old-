from django.urls import path
from . import views


app_name = 'performer'
urlpatterns = [
    path('', views.all_performers, name='all_performers'),
    path('<int:performer_id>/', views.detail, name='detail'),
    path('<int:performer_id>/leave_review/', views.leave_review, name='leave_review'),

    path('catalog/group/<str:name>/', views.catalog_find, {'find':'group'}, name='group'),
    path('catalog/specialization/<str:name>/', views.catalog_find, {'find':'specialization'}, name='specialization'),
    path('catalog/performer/<str:name>/', views.catalog_find, {'find':'performer'}, name='performer'),
    path('catalog/country/<str:name>/', views.catalog_find, {'find':'country'}, name='country'),
    path('catalog/province/<str:name>/', views.catalog_find, {'find':'province'}, name='province'),
    path('catalog/city/<str:name>/', views.catalog_find, {'find':'city'}, name='city'),

]
