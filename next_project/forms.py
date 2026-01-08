from django import forms
from .models import Contact, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'address']
        labels = {
            'address': 'Address (Optional)',
            'phone': 'Phone (Optional)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].required = False
        self.fields['phone'].required = False


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(
                attrs={'Placeholder': 'Enter your password'}
            ),
            'password2': forms.PasswordInput(
                attrs={'Placeholder': 'Enter your password'}
            ),
            'username': forms.TextInput(
                attrs={'Placeholder': 'Enter your name'}
            ),
            'email': forms.TextInput(
                attrs={'Placeholder': 'Enter your email'}
            )
        }


class LoginForm(forms.Form):
    name = forms.CharField(max_length=20, label="Username")
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password'}),
        label="Password"
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(
                attrs={'class': 'form-control',
                                'rows': 3,
                                'placeholder': 'Type your comment here...'})
        }
