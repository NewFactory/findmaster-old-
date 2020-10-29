from django.contrib import admin
from .models import Performer, Review, Group, Specialization, Phone, Email

admin.site.register(Group)
admin.site.register(Phone)
admin.site.register(Email)


class PerformerAdmin(admin.ModelAdmin):
    list_filter = ('name', 'specializations', 'cities', 'provinces')
admin.site.register(Performer, PerformerAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('performers','email', 'autor', 'create_date')
admin.site.register(Review, ReviewAdmin)

class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name','groups')
admin.site.register(Specialization, SpecializationAdmin)
