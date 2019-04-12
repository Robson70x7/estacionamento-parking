from django.urls import path, include

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home' ),
    path('pessoas/', views.lista_pessoas, name='lista_pessoas'),
    path('pessoa-novo/', views.pessoa_novo, name='pessoa-novo'),
    path('veiculos/', views.lista_veiculos, name='lista_veiculos'),
    path('veiculo-novo/', views.veiculo_novo, name='veiculo_novo'),
    path('mov-rotativos/', views.lista_movrotativos, name='lista_movrotativos'),
    path('movrotativo-novo/', views.movrotativo_novo, name='movrotativo_novo'),
    path('mensalistas/', views.lista_mensalistas, name='lista_mensalistas'),
    path('mov-mensalistas/', views.lista_movmensalistas,
            name='lista_movmensalistas'),
    
]