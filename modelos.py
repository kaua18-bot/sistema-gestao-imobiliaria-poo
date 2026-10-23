"""Modelos de domínio do Sistema de Gestão Imobiliária."""

from datetime import date
from modelos_base import Imovel


class Cliente:
    """Cliente que pode participar de várias negociações."""

    def __init__(self, nome, cpf, telefone):
        if not isinstance(nome, str) or len(nome.strip()) < 3:
            raise ValueError("O nome deve ter pelo menos 3 caracteres.")
        if not isinstance(cpf, str) or not cpf.strip():
            raise ValueError("O CPF deve ser informado.")
        if not isinstance(telefone, str) or not telefone.strip():
            raise ValueError("O telefone deve ser informado.")

        self.__nome = nome.strip()
        self.__cpf = cpf.strip()
        self.__telefone = telefone.strip()
        self.__negociacoes = []

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_telefone(self):
        return self.__telefone

    def get_negociacoes(self):
        return self.__negociacoes.copy()

    def adicionar_negociacao(self, negociacao):
        if negociacao not in self.__negociacoes:
            self.__negociacoes.append(negociacao)

    def __str__(self):
        return f"Cliente: {self.__nome} | CPF: {self.__cpf} | Telefone: {self.__telefone}"


class Contrato:
    """Contrato criado e mantido dentro de uma negociação."""

    def __init__(self, valor, tipo="Compra e venda"):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool) or valor <= 0:
            raise ValueError("O valor do contrato deve ser maior que zero.")
        if not isinstance(tipo, str) or len(tipo.strip()) < 3:
            raise ValueError("Informe um tipo de contrato válido.")

        self.__valor = float(valor)
        self.__tipo = tipo.strip()
        self.__data_assinatura = date.today()
        self.__assinado = False

    def get_valor(self):
        return self.__valor

    def get_tipo(self):
        return self.__tipo

    def get_data_assinatura(self):
        return self.__data_assinatura

    def esta_assinado(self):
        return self.__assinado

    def assinar(self):
        self.__assinado = True

    def __str__(self):
        situacao = "assinado" if self.__assinado else "aguardando assinatura"
        return (
            f"Contrato de {self.__tipo} | Valor: R$ {self.__valor:,.2f} | "
            f"Data: {self.__data_assinatura.strftime('%d/%m/%Y')} | {situacao}"
        )


class Negociacao:
    """Relaciona um cliente a um imóvel e possui seu próprio contrato."""

    def __init__(self, cliente, imovel, valor_negociado, tipo="Compra e venda"):
        if not isinstance(cliente, Cliente):
            raise TypeError("A negociação precisa estar associada a um Cliente.")
        if not isinstance(imovel, Imovel):
            raise TypeError("A negociação precisa estar associada a um Imovel.")
        if (
            not isinstance(valor_negociado, (int, float))
            or isinstance(valor_negociado, bool)
            or valor_negociado <= 0
        ):
            raise ValueError("O valor negociado deve ser maior que zero.")

        self.__cliente = cliente
        self.__imovel = imovel
        self.__valor_negociado = float(valor_negociado)
        self.__status = "Em andamento"
        self.__contrato = Contrato(self.__valor_negociado, tipo)
        cliente.adicionar_negociacao(self)

    def get_cliente(self):
        return self.__cliente

    def get_imovel(self):
        return self.__imovel

    def get_valor_negociado(self):
        return self.__valor_negociado

    def get_status(self):
        return self.__status

    def get_contrato(self):
        return self.__contrato

    def concluir(self):
        self.__status = "Concluída"
        self.__contrato.assinar()

    def cancelar(self):
        if self.__status == "Concluída":
            raise ValueError("Uma negociação concluída não pode ser cancelada.")
        self.__status = "Cancelada"

    def __str__(self):
        return (
            f"Negociação: {self.__status}\n"
            f"{self.__cliente}\n"
            f"{self.__imovel}\n"
            f"Valor negociado: R$ {self.__valor_negociado:,.2f}\n"
            f"{self.__contrato}"
        )
