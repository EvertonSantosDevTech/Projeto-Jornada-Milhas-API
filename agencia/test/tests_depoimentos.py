from rest_framework.test import APITestCase
from agencia.models import Depoimento
from django.urls import reverse
from rest_framework import status


class DepoimentosTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Depoimentos-list')
        self.Depoimento_1 = Depoimento.objects.create(
            nome_completo='Nome Test1',
            data_de_registro='2023-01-30',
            depoimento_descricao='Ótima viagem Moscou',
            # foto = null
        )

        self.Depoimento_2 = Depoimento.objects.create(
            nome_completo='Nome Test2',
            data_de_registro='2023-09-20',
            depoimento_descricao='Perfeita viagem Flórida',
            # foto = null
        )

    def test_requisicao_get_para_listar_depoimentos(self):
        """Test para verificar requisição GET para listar depoimentos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_depoimentos(self):
        """Test para verificar requisição POST para incluir depoimentos"""
        data = {
            'nome_completo': 'Nome Test3',
            'data_de_registro': '2021-10-20',
            'depoimento_descricao': 'Perfeita viagem Inglaterra'
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_deletar_depoimentos(self):
        """Test para verificar requisição DELETE para deletar depoimentos"""
        reponse = self.client.delete('/depoimentos/1/')
        self.assertEquals(reponse.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_PUT_para_atualizar_depoimentos(self):
        """Test para verificar requisição PUT para atualizar depoimentos"""
        data = {
            'nome_completo': 'Nome Test8',
            'data_de_registro': '2022-10-20',
            'depoimento_descricao': 'Perfeita viagem para o Japão'
        }
        reponse = self.client.put('/depoimentos/2/', data=data)
        self.assertEquals(reponse.status_code, status.HTTP_200_OK)
