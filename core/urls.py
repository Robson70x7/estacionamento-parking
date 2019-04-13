from django.urls import path, include

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home' ),
    # Pessoas
    path('pessoas/', views.lista_pessoas, name='lista_pessoas'),
    path('pessoa-novo/', views.pessoa_novo, name='pessoa-novo'),
    path('pessoa-update/<int:pk>', views.pessoa_update, name="pessoa_update"),

    # Veiculos
    path('veiculos/', views.lista_veiculos, name='lista_veiculos'),
    path('veiculo-novo/', views.veiculo_novo, name='veiculo_novo'),
    path('veiculo-update/<int:pk>', views.veiculo_update, name='veiculo_update'),

    # Movimento Rotativo
    path('mov-rotativos/', views.lista_movrotativos, name='lista_movrotativos'),
    path('movrotativo-novo/', views.movrotativo_novo, name='movrotativo_novo'),
    path('movrotativo-update/<int:pk>', views.movrotativo_update, name='movrotativo_update'),


    # Mensalista
    path('mensalistas/', views.lista_mensalistas, name='lista_mensalistas'),
    path('mensalista-novo/', views.mensalista_novo, name='mensalista_novo'),
    path('mensalista-update/<int:pk>', views.mensalista_update, name='mensalista_update'),

    # Movimento Mensalista
    path('mov-mensalistas/', views.lista_movmensalistas, name='lista_movmensalistas'),
    path('mov-mensalista-novo/', views.movmesalista_novo, name='movmensalista_novo'),
    path('mov-mensalista-update/<int:pk>', views.movmensalista_update, name='movmensalista_update'),
]


# IMPLEMENTAR A FUNÇÃO DELETE