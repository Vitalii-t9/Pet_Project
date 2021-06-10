from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anouns', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
             'class': 'form-control',
             'placeholder': "Article's name"
            }),
            "anouns": TextInput(attrs={
             'class': 'form-control',
             'placeholder': "Article's anouns"
            }),
            "date": DateTimeInput(attrs={
             'class': 'form-control',
             'placeholder': "Published date"
            }),
            "full_text": Textarea(attrs={
             'class': 'form-control',
             'placeholder': "Article's text"
            })

        }