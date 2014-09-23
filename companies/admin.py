from django.conf import settings
from django.contrib import admin
from django.core.exceptions import ValidationError
from companies.models import *
from django.forms import ModelForm, RegexField
from suit_ckeditor.widgets import CKEditorWidget
from django.utils.translation import ugettext as _
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    prepopulated_fields = {"slug": ("name",)}


class PageForm(ModelForm):
    class Meta:
        widgets = {
            'description': CKEditorWidget(editor_options={'startupFocus': True})
        }

#class SimplePageForm(ModelForm):
#    class Meta:
#       widgets = {
#            'page': CKEditorWidget(editor_options={'startupFocus': True})
#       }

class AddressInline(admin.TabularInline):
    model = Address
    extra = 0

class CompanyAdmin(admin.ModelAdmin):
    form = PageForm
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = [
        (None, {'fields': ['name', 'meta_words', 'email', 'site', 'phone', 'image', 'subcategory', 'on_map', 'slug',
                           'recommendations', 'person', 'accepted']}),

        (_('Description'), {'classes': ('full-width',), 'fields': ('description', )})
    ]
    inlines = [
        AddressInline,
    ]

#class SimplePageAdmin(admin.ModelAdmin):
#    prepopulated_fields = {"slug": ("title",)}
#    form = SimplePageForm

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, CategoryAdmin)
admin.site.register(Company, CompanyAdmin)
#admin.site.register(SimplePage, SimplePageAdmin)