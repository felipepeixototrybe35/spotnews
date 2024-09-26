from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Nome',
        }
        widgets = {
            'name': forms.TextInput(attrs={'maxlength': 200, 'required': True}),
        }
