from django.shortcuts import render


def index(request):
    return render(request, "next_project/index.html")


def detail(request):
    return render(request, "next_project/detail.html")


def about(request):
    return render(request, "next_project/about.html")


def login(request):
    return render(request, "next_project/login.html")


def logout(request):
    return render(request, "next_project/logout.html")


def register(request):
    return render(request, "next_project/register.html")