from django.db.models import Q
from django.template.response import TemplateResponse
from companies.models import Category, SubCategory, Company


def index(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    response = TemplateResponse(
        request=request,
        context=context,
        template="main.html"
    )
    return response


def company_list(request, subcat_id):
    subcat = SubCategory.objects.get(id=subcat_id)
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

def company_one(request, company_id):
    company = Company.objects.get(id=company_id)
    categories = Category.objects.all()
    context = {
        'company': company,
        'categories': categories
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
    q_companies = []
    for company in companies:
        if query in company.name.lower() or query in company.description.lower():
            q_companies.append(company)
    #q_companies = Company.objects.filter(Q(name__icontains=query.lower()) | Q(description__icontains=query.lower()))
    context = {
        'companies': q_companies
    }
    response = TemplateResponse(
        request=request,
        context=context,
        template="main.html"
    )
    return response

