from django.shortcuts import get_object_or_404, render
from .models import News


def home_view(request):
    news = News.objects.all()  # Obter todas as notícias do banco de dados
    return render(request, 'home.html', {'news': news})


def news_details_view(request, id):
    news_item = get_object_or_404(News, id=id)
    return render(request, 'news_details.html', {'news_item': news_item})

