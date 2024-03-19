from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    page = Paginator(products, 6)
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = page.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = page.page(1)
    except EmptyPage:
        page_obj = page.page(page.num_pages)

    return render(request, "index.html", {"products" : page_obj })


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, "index2.html", {"product":product})


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)
    return render(request, "edit.html", {"form":form})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.delete()
        return redirect("product_list")
    return render(request, "delete.html", {'product':product})

