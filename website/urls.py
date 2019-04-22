from django.urls import include, path
from . import views

app_name = "website"

urlpatterns = [
    path('', views.home, name="home"),
    path('contato/', views.contato, name="contato"),
    path('contato/<mensagem>', views.contato, name="contato"),
    path('save_contato/', views.save_contato, name="save_contato"),
    path('servico/', views.servico, name="servico"),
]