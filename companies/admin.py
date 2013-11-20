from django.contrib import admin
from companies.models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Company)
