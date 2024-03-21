from django import forms
from .models import Product, Contact

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', "image"]

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'subject', 'message']

        widgets ={
            "full_name": forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'subject': forms.TextInput(attrs={'class':'form-control'}),
            'message': forms.Textarea(attrs={'class':'form-control'}),
        }
