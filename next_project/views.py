from django.shortcuts import render


def index(request):
    return render(request, "next_project/index.html", {'active_tab': 'index'})


def detail(request):
    return render(request,
                  "next_project/detail.html", {'active_tab': 'detail'})


def about(request):
    return render(request, "next_project/about.html", {'active_tab': 'about'})


def login(request):
    return render(request, "next_project/login.html", {'active_tab': 'login'})


def logout(request):
    return render(request,
                  "next_project/logout.html", {'active_tab': 'logout'})


def register(request):
    return render(request,
                  "next_project/register.html", {'active_tab': 'register'})
