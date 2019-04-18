from django.urls import include, path
from . import views

app_name = "website"

urlpatterns = [
    path('', views.home, name="home"),
    path('contato/', views.contato, name="contato"),
    path('servico/', views.servico, name="servico"),
]