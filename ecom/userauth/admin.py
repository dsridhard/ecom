from django.contrib import admin
from .models import Userauth

# Register your models here.

class UserauthAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "phone","joined_date",)

admin.site.register(Userauth,UserauthAdmin)