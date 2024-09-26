from django.shortcuts import get_object_or_404, redirect, render
from .models import News
from .forms import CategoryForm


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
