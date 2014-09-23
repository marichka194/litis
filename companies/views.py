#  -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from pytils.translit import slugify
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from companies.models import Category, SubCategory, Company, SimplePage, Address, StoredSession
from forms import ClientForm


def index(request):
    categories = Category.objects.all()
    companies = Company.objects.all().filter(accepted=True)
    context = {
        "categories": categories,
        "companies": companies,
        "sessy": request.session.session_key
    }
    response = TemplateResponse(
        request=request,
        context=context,
        template="base_company.html"
    )
    return response


def company_list(request, subcat_slug):
    subcat = SubCategory.objects.get(slug=subcat_slug)
    categories = Category.objects.all()
    companies = subcat.company_set.all()
    context = {
        "categories": categories,
        'companies': companies,
        'active_category': subcat
    }
    response = TemplateResponse(
        request=request,
        context=context,
        template="main.html"
    )
    return response

def company_one(request, company_slug):
    company = Company.objects.get(slug=company_slug)
    subcat = company.subcategory
    categories = Category.objects.all()
    context = {
        'company': company,
        'categories': categories,
        'active_category': subcat
    }
    response = TemplateResponse(
        request=request,
        context=context,
        template="company.html"
    )
    return response

def search(request):
    query = request.GET.get('search', None)
    companies = Company.objects.all()
    categories = Category.objects.all()
    q_companies = []
    for company in companies:
        if query in company.name.lower() or query in company.description.lower() or query in company.meta_words.lower():
            q_companies.append(company)
    #q_companies = Company.objects.filter(Q(name__icontains=query.lower()) | Q(description__icontains=query.lower()))
    context = {
        'companies': q_companies,
        'categories': categories,
    }
    response = TemplateResponse(
        request=request,
        context=context,
        template="main.html"
    )
    return response

def flatpage(request, slug):
    page =get_object_or_404(SimplePage, slug=slug)

    categories = Category.objects.all()
    context = {
        'page': page,
        'categories': categories,
    }
    response = TemplateResponse(
        request=request,
        context=context,
        template="main.html"
    )
    return response

def about_us(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    response = TemplateResponse(
        request=request,
        context=context,
        template="about_us.html"
    )
    return response

def contacts(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    response = TemplateResponse(
        request=request,
        context=context,
        template="contacts.html"
    )
    return response

def add_company(request):
    categories = Category.objects.all()
    form = None
    addresses_fields = [x for x in request.POST.keys() if 'address' in x]
    if request.method == "POST":
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            company.slug = slugify(company.name)
            company.accepted = False
            company.save()

            addresses = [Address(address=request.POST[a], company=company) for a in addresses_fields]
            for a in addresses:
                a.save()
            subject = u'Новая заявка'
            mail = u"""
            Новая заявка в категорию {category}. Новая компания - {company}
            """.format(category=company.subcategory, company=company.name)
            #recipients = [x.email for x in User.object s.filter(is_superuser=True)]
            recipients = ["litisproject@gmail.com"]
            send_mail(subject, mail, 'admin@litis.com.ua', recipients)
            return HttpResponseRedirect(reverse('company', args=[company.slug, ]))
    else:
        form = ClientForm()
    context = {
        'categories': categories,
        'form': form
    }
    response = TemplateResponse(
        request=request,
        context=context,
        template="client_form.html"
    )
    return response

def voting(request, company_slug, rate):
    company = Company.objects.get(slug=company_slug)
    has_voted = False
    myid = str(request.session.session_key)
    sess = company.storedsession_set.filter(session_id=myid)
    if len(sess) == 0:
        s = StoredSession()
        s.session_id = myid
        s.company = company
        s.save(True)
        rate = int(rate)
        company.sum_rating += rate
        company.voted += 1
        company.rating = float(float(company.sum_rating)/company.voted)
        company.save()
    else:
        has_voted = True
    context = {
        'company': company,
        'has_voted': has_voted
    }
    response = TemplateResponse(
        request=request,
        context=context,
        template="company.html"
    )
    return response