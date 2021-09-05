from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'

    sorting_name = request.GET.get("sort")
    phones = Phone.objects.all()

    if sorting_name == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sorting_name == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    elif sorting_name == 'name':
        phones = Phone.objects.all().order_by('name')

    context = {"phones":phones}
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    context = {'phone':Phone.objects.get(slug=slug)}
    return render(request, template, context)

