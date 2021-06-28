from django.contrib import admin
from .models import Contact

# Register your models here.
admin.site.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id','fname','address','message']
