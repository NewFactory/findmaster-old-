from django.contrib import admin
from .models import Performer, Review, Specialization

# Register your models here.
admin.site.register(Specialization)
admin.site.register(Performer)
admin.site.register(Review)
