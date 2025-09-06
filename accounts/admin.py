from django.contrib import admin
from .models import Category, SubCategory, FieldName, FieldPhoto

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(FieldName)
admin.site.register(FieldPhoto)
