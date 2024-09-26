from django import forms
from .models import Category, News


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Nome',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={'maxlength': 200, 'required': True}
                ),
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'title', 'content', 'author', 'created_at', 'image', 'categories'
            ]
        labels = {
            'title': 'Título',
            'content': 'Conteúdo',
            'author': 'Autoria',
            'created_at': 'Criado em',
            'image': 'URL da Imagem',
            'categories': 'Categorias',
        }
        widgets = {
            'title': forms.TextInput(attrs={'maxlength': 200, 'required': True}),
            'content': forms.Textarea(attrs={'required': True}),
            'author': forms.Select(),
            'created_at': forms.DateInput(attrs={'type': 'date'}),
            'image': forms.FileInput(attrs={'required': False}),
            'categories': forms.CheckboxSelectMultiple(),  # Checkbox mult cat
        }
