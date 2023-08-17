from rest_framework.test import APITestCase
from agencia.models import Destino
from django.urls import reverse
from rest_framework import status

class DestinosTests(APITestCase):
    def setUp(self):
        self.list_url = reverse('Destinos-list')
        self.Destino_1 = Destino.objects.create(
            nome='Nome Destino 1 Teste',
            preco=2000,
            meta='Lugar muito maravilhoso'
            depoimento_descricao='Ótima viagem Moscou',
            texto_descritivo='interessante'
            # foto = null
        )

        self.Destino_2 = Destino.objects.create(
            nome='Nome Destino 2 Teste',
            preco=8000,
            meta='Lugar Perfeito'
            depoimento_descricao='viagem adorável',
            texto_descritivo='pois é maravilhoso'
            # foto = null
        )

    def test_requisicao_get_para_listar_destinos(self):
        """Test para verificar requisição GET para listar destinos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    
    def test_requisicao_post_para_criar_destinos(self):
        """Test para verificar requisição POST para incluir destinos"""
        data = {
            'nome': 'Nome de destino Test3',
            'preco': '3500.23',
            'depoimento_descricao': 'Perfeita viagem Inglaterra',
            'meta': 'Lugar mais que perfeito',
            'depoimento_descricao' : 'Boa perfeita e agradável',
            'texto_descritivo' : 'certamente inesquecível'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_deletar_destinos(self):
        """Test para verificar requisição DELETE para deletar destinos"""
        reponse = self.client.delete('/destinos/1/')
        self.assertEquals(reponse.status_code, status.HTTP_204_NO_CONTENT)

