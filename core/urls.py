from django.urls import path, include

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home' ),
    path('pessoas/', views.listar_pessoas, name='listar_pessoa'),
    path('veiculos/', views.listar_veiculos, name='listar_veiculos'),
    path('mov-rotativo/', views.listar_movrotativos, name='listar_mov_rot'),
]