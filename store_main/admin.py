from django.contrib import admin
from .models import Products, Category, UserCart, Feedback, Sale

# Register your models here.
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(UserCart)
admin.site.register(Feedback)
admin.site.register(Sale)
