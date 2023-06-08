from django import forms
from .models import product

class ArticleForm(forms.ModelForm):
    class Meta:
        model= product
        fields = ['title', 'category', 'price', 'description','image']
        labels = {'title': 'Titre', 'category': 'category', 'price': 'prix',
                  'description': 'description'}
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            
            
        }  
        
        