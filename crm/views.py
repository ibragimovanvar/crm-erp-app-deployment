from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
def index(request):
    return render(request, 'crm/index.html')


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'crm/add-product.html', {'form': form})


def view_products(request, category):
    products = Product.objects.filter(category=category)
    return render(request, f'crm/{category}.html', {'products': products})

