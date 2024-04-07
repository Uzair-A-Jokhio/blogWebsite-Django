from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from .forms import ProductForm, ContactForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse
# Create your views here.

class AddCategoryview(generic.CreateView):
    model = Category
    template_name = 'add_category.html'
    fields ="__all__"

def cateogry_views(request, cats):
    category_list = Product.objects.filter(category=cats.replace('-', ' '))
    return render(request, "categories.html", {"cats":cats.title().replace('-', ' '), "category_list":category_list})

def category_list_view(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {"cat_menu_list":cat_menu_list})

def LikeView(request, pk):
    post = get_object_or_404(Product, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('product_detail', args=[str(pk)]))


class HomeView(generic.ListView):
    model = Product
    template_name = "index.html"
    paginate_by = 9
    cats = Category.objects.all()

    def get_context_data(self, *args ,**kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data( *args ,**kwargs)
        context["cat_menu"] = cat_menu
        return context

class ArticalDetailView(generic.DetailView):
    model = Product
    template_name = "index2.html"

    def get_context_data(self, *args ,**kwargs):
        stuff = get_object_or_404(Product, id=self.kwargs['pk'])
        total_likes = stuff.total_likes() # function from models 

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context = super(ArticalDetailView, self).get_context_data( *args ,**kwargs)

        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


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
        