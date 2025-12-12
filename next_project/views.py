from django.shortcuts import render, redirect
from .forms import ContactForm, RegisterForm
from django.contrib import messages


def index(request):
    return render(request, "next_project/index.html", {'active_tab': 'index'})


def detail(request):
    return render(request,
                  "next_project/detail.html", {'active_tab': 'detail'})


def about(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                'next_project/about.html',
                {
                    'form': ContactForm(),
                    'success': True
                }
            )
    else:
        form = ContactForm()
    return render(request,
                  "next_project/about.html",
                  {'active_tab': 'about', 'form': form})


def login(request):
    return render(request, "next_project/login.html", {'active_tab': 'login'})


def logout(request):
    return render(request,
                  "next_project/logout.html", {'active_tab': 'logout'})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('name')
            messages.success(
                request, f'Account created for {username}! You can now log in.'
            )
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request,
                  "next_project/register.html", {
                      'form': form, 'active_tab': 'register'})
