from django.contrib import admin
from companies.models import *
from django.forms import ModelForm
from suit_ckeditor.widgets import CKEditorWidget
from django.utils.translation import ugettext as _

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]




class PageForm(ModelForm):
    class Meta:
        widgets = {
            'description': CKEditorWidget(editor_options={'startupFocus': True})
        }


class CompanyAdmin(admin.ModelAdmin):
    form = PageForm
    fieldsets = [
        (None, {'fields': ['name', 'address', 'rating', 'image', 'subcategory', 'on_map']}),

        (_('Description'), {'classes': ('full-width',), 'fields': ('description', )})
    ]

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Company, CompanyAdmin)