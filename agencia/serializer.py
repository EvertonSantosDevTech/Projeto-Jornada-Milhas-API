from rest_framework import serializers
from agencia.models import Depoimento, Destino


class DepoimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depoimento
        fields = ['id', 'nome_completo', 'data_de_registro',
                  'depoimento_descricao', 'foto']


# class ListaDepoimentosSelecionadosSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Depoimento
#        fields = ['id', 'nome_completo', 'data_de_registro',
#                  'depoimento_descricao', 'foto']


class DestinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = ['id', 'nome', 'preco', 'foto1']


class DestinoSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = ['id', 'nome', 'preco', 'foto1',
                  'foto2', 'meta', 'texto_descritivo']
