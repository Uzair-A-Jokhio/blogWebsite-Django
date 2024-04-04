from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from .forms import ProductForm, ContactForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


from django.views import generic
# Create your views here.

class AddCategoryview(generic.CreateView):
    model = Category
    template_name = 'add_category.html'
    fields ="__all__"

def cateogry_views(request, cats):
    category_list = Product.objects.filter(category=cats.replace('-', ' '))
    return render(request, "categories.html", {"cats":cats.title().replace('-', ' '), "category_list":category_list})


def product_list(request):
    products = Product.objects.all().order_by('-id')  # Retrieve all products and reverse their order
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


def product_detail(request, pk):    # show the details if individual products
    product = Product.objects.get(pk=pk)
    return render(request, "index2.html", {"product":product})


def edit_product(request, pk): 
    """   """
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)
    return render(request, "edit.html", {"form":form, 'product':product})


def delete_product(request, pk):
    ''' The function Delete's the blog page '''
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.delete()
        return redirect("product_list")
    return render(request, "delete.html", {'product':product})

@login_required
def post_blog(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect('product_detail', pk=product.id)
    else:
        form = ProductForm()
    return render(request, 'post_blog.html', {"form":form, "errors": form.errors})

def contact_page(request):
    
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('contact_page')
    context = {"form":form}
    return render(request, 'contact.html', context)

def about_page(request):
    return render(request, 'about_us.html',{})


def search_bar(request):
    """ this fuction is used in search-bar,
        -it looks for the parameter 'searched'
     
        then return two dict values searched and blogs   """

    if request.method == "POST":
        searched = request.POST['searched'] #looks for anything in search bar
        blogs = Product.objects.filter(name__contains=searched)  #filter out the searched product by name
        return render(request, 'search_thing.html', {'searched':searched, 'blogs':blogs})
    else:
        return render(request, 'search_thing.html', {'searched':searched})
        