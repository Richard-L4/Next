from django.shortcuts import render, redirect
from .forms import ContactForm, RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import CardText
from django.core.paginator import Paginator


def index(request):
    return render(request, "next_project/index.html",
                  {'active_tab': 'index'})


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


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, "next_project/login.html", {'active_tab': 'login',
                                                       'form': form})


@login_required(login_url='login')
def user_logout(request):
    return render(request,
                  "next_project/logout.html", {'active_tab': 'logout'})


def confirm_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
    return render(request,
                  "next_project/confirm_logout.html",
                  {'active_tab': 'confirm_logout'})


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


def detail_view(request):
    lang = request.GET.get('lang', 'en')

    card_text = CardText.objects.all()
    paginator = Paginator(card_text, 1)  # 1 card per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Get the card on this page
    card = page_obj[0] if page_obj else None

    if card:
        translation = card.translations.filter(language=lang).first()
        content = translation.content if translation else (
            card.content or 'Content coming soon.')
    else:
        # Fallback card if no cards exist
        card = type('Card', (), {
            'title': 'Coming Soon',
            'image_name': 'placeholder.png',
            'content': 'This card will be available soon.'
        })()
        content = card.content

    return render(request, "next_project/detail.html", {
        'card': card,
        'content': content,
        'active_tab': 'detail',
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    })
