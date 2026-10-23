"""Testes automatizados do Sistema de Gestão Imobiliária."""

import unittest
from modelos_base import Imovel
from modelos import Cliente, Contrato, Negociacao


class TestSistemaImobiliario(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente("Maria Oliveira", "12345678900", "19999990000")
        self.imovel = Imovel("Rua das Flores, 123", 350000, "apartamento")

    def test_imovel_valido(self):
        self.assertEqual(self.imovel.get_endereco(), "Rua das Flores, 123")
        self.assertEqual(self.imovel.get_preco(), 350000.0)
        self.assertEqual(self.imovel.get_tipo(), "apartamento")

    def test_setter_imovel_preserva_valor_invalido(self):
        endereco_original = self.imovel.get_endereco()
        preco_original = self.imovel.get_preco()
        tipo_original = self.imovel.get_tipo()

        self.imovel.set_endereco("abc")
        self.imovel.set_preco(-10)
        self.imovel.set_tipo("castelo")

        self.assertEqual(self.imovel.get_endereco(), endereco_original)
        self.assertEqual(self.imovel.get_preco(), preco_original)
        self.assertEqual(self.imovel.get_tipo(), tipo_original)

    def test_cliente_inicia_sem_negociacoes(self):
        self.assertEqual(self.cliente.get_negociacoes(), [])

    def test_negociacao_vincula_cliente_e_imovel(self):
        negociacao = Negociacao(self.cliente, self.imovel, 340000)
        self.assertIs(negociacao.get_cliente(), self.cliente)
        self.assertIs(negociacao.get_imovel(), self.imovel)
        self.assertEqual(len(self.cliente.get_negociacoes()), 1)

    def test_contrato_e_criado_na_negociacao(self):
        negociacao = Negociacao(self.cliente, self.imovel, 340000)
        self.assertIsInstance(negociacao.get_contrato(), Contrato)
        self.assertEqual(negociacao.get_contrato().get_valor(), 340000.0)
        self.assertFalse(negociacao.get_contrato().esta_assinado())

    def test_concluir_assina_contrato(self):
        negociacao = Negociacao(self.cliente, self.imovel, 340000)
        negociacao.concluir()
        self.assertEqual(negociacao.get_status(), "Concluída")
        self.assertTrue(negociacao.get_contrato().esta_assinado())

    def test_nao_permite_valor_negociado_invalido(self):
        with self.assertRaises(ValueError):
            Negociacao(self.cliente, self.imovel, 0)

    def test_nao_permite_cliente_invalido(self):
        with self.assertRaises(TypeError):
            Negociacao("Maria", self.imovel, 1000)


if __name__ == "__main__":
    unittest.main(verbosity=2)
