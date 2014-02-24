__author__ = 'Masha'
from django.conf.urls import patterns, include, url
from views import index, company_list, company_one, search

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^subcat/(?P<subcat_id>\d+)/', company_list, name='subcat_list'),
    url(r'^company/(?P<company_id>\d+)/', company_one, name='company'),
    url(r'^search/', search, name='search')
)