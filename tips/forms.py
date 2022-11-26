from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from tips.models import TipsArticle

class DateInput(forms.DateInput):
    input_type = 'date'
    
class AddArticle(forms.ModelForm):
    class Meta:
        model = TipsArticle
        fields = ["title", "content", "publish", "image"]

        title = forms.CharField(max_length='250', required=True)
        content = forms.Textarea()

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type article content here..'}),
            'publish': DateInput(),
        }
        
