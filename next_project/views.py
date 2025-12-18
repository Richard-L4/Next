from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm, RegisterForm, CommentForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import CardText, Comment
from django.core.paginator import Paginator
from django.http import HttpResponseBadRequest


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

    # -------------------- CARD PAGINATION --------------------
    cards = CardText.objects.all()
    card_paginator = Paginator(cards, 1)
    card_page_number = request.GET.get('page')
    card_page_obj = card_paginator.get_page(card_page_number)
    card = card_page_obj.object_list[0] if card_page_obj.object_list else None

    if card:
        # Card content
        translation = card.translations.filter(language=lang).first()
        content = translation.content if translation else (card.content or 'Content coming soon.')

        # Comments
        comments_qs = Comment.objects.filter(CardText=card).order_by('-created_at')
        comment_paginator = Paginator(comments_qs, 5)
        comment_page_number = request.GET.get('comments_page')
        comments = comment_paginator.get_page(comment_page_number)

        comment_form = CommentForm()

        # -------------------- HANDLE POST --------------------
        if request.method == 'POST':
            if 'add_comment' in request.POST:
                comment_form = CommentForm(request.POST)
                if comment_form.is_valid():
                    new_comment = comment_form.save(commit=False)
                    new_comment.CardText = card  # attach card (note the field name)
                    new_comment.user = request.user
                    new_comment.save()
                    return redirect(f"{request.path}?page={card_page_obj.number}")

            elif 'edit_comment' in request.POST:
                comment_id = request.POST.get('comment_id')
                comment = get_object_or_404(Comment, id=comment_id, user=request.user)
                comment_form = CommentForm(request.POST, instance=comment)
                if comment_form.is_valid():
                    comment_form.save()
                    return redirect(f"{request.path}?page={card_page_obj.number}")

            elif 'delete_comment' in request.POST:
                comment_id = request.POST.get('comment_id')
                comment = get_object_or_404(Comment, id=comment_id, user=request.user)
                comment.delete()
                return redirect(f"{request.path}?page={card_page_obj.number}")

    else:
        # No card found, fallback
        card = type('Card', (), {
            'title': 'Coming Soon',
            'image_name': 'placeholder.png',
            'content': 'This card will be available soon.'
        })()
        content = card.content
        comments = []
        comment_form = None

    context = {
        'card': card,
        'content': content,
        'page_obj': card_page_obj,
        'is_paginated': card_page_obj.has_other_pages() if card_page_obj else False,
        'comments': comments,
        'comment_form': comment_form,
        'active_tab': 'detail',
    }

    return render(request, 'next_project/detail.html', context)
