from django.shortcuts import render
from .models import News


def home_view(request):
    news = News.objects.all()  # Obter todas as notícias do banco de dados
    return render(request, 'home.html', {'news': news})
