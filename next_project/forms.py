from django import forms
from .models import Contact, Register


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


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['name', 'email', 'password', 'address']
        widgets = {
            'password': forms.PasswordInput(
                attrs={'Placeholder': 'Enter your password'}
            ),
            'name': forms.TextInput(
                attrs={'Placeholder': 'Enter your name'}
            ),
            'email': forms.TextInput(
                attrs={'Placeholder': 'Enter your email'}
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].required = False
