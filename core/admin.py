from django.contrib import admin
from .models import Pessoa, Marca, Veiculo, Parametros, MovRotativo, Mensalista, MovMensalista

class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'checkin', 'checkout', 'hora_total', 'total','status')

class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ('mensalista','data_pagamento', 'total')


admin.site.register(Pessoa)
admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Parametros)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, MovMensalistaAdmin)
admin.site.register(MovRotativo, MovRotativoAdmin)

