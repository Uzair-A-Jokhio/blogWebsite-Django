from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def login_user(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f"Welcome {username} ")
            return redirect('product_list')
        else:
            messages.info(request, f"Username and password not valid or Account dosen't exists!!! ")
            return redirect('login')
    
    return render(request, 'authen/login.html', {})

def logout_user(request):
    logout(request)
    messages.info(request, "You have been Logged OUT")
    return redirect('product_list')