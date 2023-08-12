from django.contrib import admin
from agencia.models import Depoimento


class Depoimentos(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'data_de_registro',
                    'depoimento_descricao')
    list_display_links = ('id', 'nome_completo')
    search_fields = ('nome_completo',)
    list_per_page = 3


admin.site.register(Depoimento, Depoimentos)
