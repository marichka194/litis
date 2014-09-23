__author__ = 'Masha'
from django.conf.urls import patterns, include, url
from views import index, company_list, company_one, search, flatpage, about_us, add_company, contacts, voting

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^subcat/(?P<subcat_slug>[\w-]+)/', company_list, name='subcat_list'),
    url(r'^company/(?P<company_slug>[\w-]+)/', company_one, name='company'),
    url(r'^search/', search, name='search'),
    url(r'^pages/(?P<slug>[\w-]+)/', flatpage, name='flatpage'),
    url(r'^about_us/', about_us, name='about_us'),
    url(r'^contacts/', contacts, name='contacts'),
    url(r'^add_company', add_company, name='add_company'),
    url(r'^vote/(?P<company_slug>[\w-]+)/(?P<rate>[0-5])/', voting, name='voting'),
)