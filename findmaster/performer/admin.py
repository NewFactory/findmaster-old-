from django.contrib import admin
from .models import Performer, Review, Group, Specialization

admin.site.register(Group)

class PerformerAdmin(admin.ModelAdmin):
    list_filter = ('name', 'specialization', 'city', 'provinces')
admin.site.register(Performer, PerformerAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('performer','email', 'autor', 'create_date')
admin.site.register(Review, ReviewAdmin)

class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name','group')
admin.site.register(Specialization, SpecializationAdmin)
