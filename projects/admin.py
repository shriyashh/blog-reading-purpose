from django.contrib import admin
from .models import Project


admin.site.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fields = ['id','title', 'description', 'technology', 'image']
