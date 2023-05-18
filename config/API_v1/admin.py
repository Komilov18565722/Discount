from django.contrib import admin
from .models import Product, My_user, Category, Business_type
# Register your models here.

admin.site.register(Product)
admin.site.register(My_user)
admin.site.register(Category)
admin.site.register(Business_type)
