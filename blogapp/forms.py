from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author','body','post']
        labels = {'author': 'Author', 'body':'Body','post':'Post'}
        widgets = {'author': forms.TextInput(attrs={'class': 'form-control'}),
                   'body': forms.TextInput(attrs={'class': 'form-control'}),
                   'post': forms.TextInput(attrs={'class': 'form-control'}),
                }
