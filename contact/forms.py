from .models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['fname','address','message']
        labels = {'fname': 'Full Name',
                  'address':'Permanent Address with Contact Number',
                  'message':'Message'}
        widgets = {'fname': forms.TextInput(attrs={'class': 'form-control'}),
                   'address': forms.Textarea(attrs={'class': 'form-control', 'rows':"2"}), 
                   'message': forms.Textarea(attrs={'class': 'form-control', 'rows':"3"}),
                }