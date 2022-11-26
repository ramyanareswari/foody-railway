from urllib import request
from homepage.models import ContactForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class FormContact(forms.ModelForm):
	class Meta:
		model = ContactForm
		fields = "__all__"
		widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama', 'required': 'true'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email', 'required': 'true'}),
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Pesan', 'required': 'true', 'spellcheck':'false'}),
		}