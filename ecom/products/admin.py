from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
  list_display = ("name", "category", "price","description","material","color","size","warranty",)
admin.site.register(Product,ProductAdmin)
