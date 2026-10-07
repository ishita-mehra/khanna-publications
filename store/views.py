from django.shortcuts import render
from django.http import Http404
from .data import CATEGORIES, get_category


def home(request):
    return render(request, 'store/home.html', {
        'categories': CATEGORIES,
    })


def category_detail(request, slug):
    cat = get_category(slug)
    if not cat:
        raise Http404("Category not found")
    return render(request, 'store/category.html', {
        'category': cat,
        'categories': CATEGORIES,
    })