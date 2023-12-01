from django.shortcuts import render, redirect
from .forms import ProductForm
from django.contrib import messages
from .models import Product


def products(request):
    all_products = Product.objects.all()
    context = {"products": all_products}
    return render(request, 'products/products.html', context)


def add_products(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Destination saved successfully')
            return redirect("add-products-url")
        else:
            messages.error(request, 'Product saving failed')
            return redirect("add-products-url")
    else:
        form = ProductForm()
    return render(request, 'products/add-products.html', {'form': form})


def update_products(request):
    return render(request, 'products/update-products.html')


def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    messages.success(request, 'Destination deleted successfully')
    return redirect('products-url')
