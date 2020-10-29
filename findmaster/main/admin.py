from django.contrib import admin
from .models import Country, Provinces, City, Status


admin.site.register(Country)
admin.site.register(Provinces)
admin.site.register(City)
admin.site.register(Status)
