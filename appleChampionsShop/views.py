from django.shortcuts import render
from products.models import Product


def home(request):
    all_products = Product.objects.all()
    context = {"products": all_products}
    return render(request, 'wander/index.html', context)
