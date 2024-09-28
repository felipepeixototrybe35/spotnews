from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets
from news.serializers import CategorySerializer, UserSerializer
from .models import Category, News, User
from .forms import CategoryForm, NewsForm


def home_view(request):
    news = News.objects.all()  # Obter todas as notícias do banco de dados
    return render(request, 'home.html', {'news': news})


def news_details_view(request, id):
    news_item = get_object_or_404(News, id=id)
    return render(request, 'news_details.html', {'news_item': news_item})


def category_form_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')  # Redireciona > home após o cadastro
    else:
        form = CategoryForm()  # Cria um formulário vazio para GET

    return render(request, 'categories_form.html', {'form': form})


def news_form_view(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)  # Para lidar com arquivos
        if form.is_valid():
            form.save()
            return redirect('home-page')  # Redireciona para a página principal
    else:
        form = NewsForm()  # Formulário vazio para o método GET

    return render(request, 'news_form.html', {'form': form})


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()  # Todas as categorias
    serializer_class = CategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Todas as pessoas usuárias
    serializer_class = UserSerializer
