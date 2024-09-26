from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home-page'),
    path('news/<int:id>/', views.news_details_view, name='news-details-page'),
    path('categories/', views.category_form_view, name='categories-form'),
    path('news/', views.news_form_view, name='news-form'),
]
