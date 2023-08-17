from rest_framework import serializers
from agencia.models import Depoimento, Destino
from bardapi import Bard
from .validators import *
import os


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

    def validate(self, data):
        if texto_descritivo_valido(data['texto_descritivo']):
            data['texto_descritivo'] = pergunta(pergunta)
        return data


class DestinoSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = ['id', 'nome', 'preco', 'foto1',
                  'foto2', 'meta', 'texto_descritivo']


def pergunta(pergunta):
    prompt = f"resumo sobre a cidade de {pergunta} em 200 caracteres"
    os.environ['_BARD_API_KEY'] = str(os.getenv('_BARD_API_KEY'))
    bard = Bard(token_from_browser=True)
    resposta = bard.get_answer(prompt)['content']
    # print(resposta)
    return resposta
