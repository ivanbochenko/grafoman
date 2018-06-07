from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('addArticle', views.addArticle, name='addArticle'),
    path('add', views.add, name='add')
]
