__author__ = 'Admin'

from django.forms import ModelForm, Textarea
from models import *

class ClientForm(ModelForm):
    class Meta:
        model = Company
        exclude = ['meta_words','on_map', 'slug', 'accepted']
        widgets = {
            'description': Textarea(attrs={'cols': 180, 'rows': 5}),
            'recommendations': Textarea(attrs={'cols': 180, 'rows': 5}),
        }


class CompanyAddressForm(ModelForm):
    class Meta:
        model = Address
        exclude = ['company']