from rest_framework import viewsets
from agencia.models import Depoimento, Destino
from agencia.serializer import DepoimentoSerializer, DestinoSerializer, DestinoSerializerV2

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework import filters
import random


class DepoimentosViewSet(viewsets.ModelViewSet):
    queryset = Depoimento.objects.all()
    serializer_class = DepoimentoSerializer


class DepoimentosSelecionadosViewSet(viewsets.ModelViewSet):
    """Exibindo 3 depoimentos aleatoriamente"""
    serializer_class = DepoimentoSerializer
    http_method_names = ['get']

    def get_queryset(self):
        depoimentos = Depoimento.objects.all()
        queryset = random.sample(list(depoimentos), k=3)
        return queryset


class DestinosViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            # serializer_class = DestinoSerializer
            return DestinoSerializerV2
        else:
            return DestinoSerializer

    def get_queryset(self):
        queryset = Destino.objects.all()
        nome_cidade = self.request.query_params.get('nome')
        if nome_cidade is not None:
            queryset = queryset.filter(nome__icontains=nome_cidade.title())

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        if not queryset.exists():
            return Response({"mensagem": "Nenhum destino foi encontrado."}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data)
