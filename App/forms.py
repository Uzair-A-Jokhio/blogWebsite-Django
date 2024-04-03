from django import forms
from .models import Product, Contact

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', "image"]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'subject', 'message']

        widgets ={
            "full_name": forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your full Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your email address'}),
            'subject': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the subject'}),
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter the message'}),
        }
