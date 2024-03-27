from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserSignupForm

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

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

def signup_user(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid:
            form.save()   
            messages.success(request, "Your account has been created! Now you can Login")
            return redirect('login')
    else:
        form = UserSignupForm()
    return render(request, 'authen/signup.html', {'form':form})


def welcome_mail(username, email):
    htmly = get_template('authen/email.html')
    d = { 'username': username }
    subject, from_email, to = 'welcome', 'your_email@gmail.com', email
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()