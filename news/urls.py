from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', views.home_view, name='home-page'),
    path('news/<int:id>/', views.news_details_view, name='news-details-page'),
    path('categories/', views.category_form_view, name='categories-form'),
    path('news/', views.news_form_view, name='news-form'),
    path("api/", include(router.urls)),
]
