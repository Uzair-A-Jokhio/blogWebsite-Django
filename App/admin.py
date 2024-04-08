from django.contrib import admin
from .models import Product, Contact, Category, Profile
# Register your models here.


admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Category)