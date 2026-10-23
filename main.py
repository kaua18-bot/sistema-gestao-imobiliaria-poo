"""Demonstração simples do Sistema de Gestão Imobiliária."""

from modelos_base import Imovel
from modelos import Cliente, Negociacao


def main():
    print("=" * 48)
    print(" SISTEMA DE GESTÃO IMOBILIÁRIA")
    print("=" * 48)

    cliente = Cliente(
        nome="Maria Oliveira",
        cpf="123.456.789-00",
        telefone="(19) 99999-0000"
    )
    imovel = Imovel(
        endereco="Rua das Flores, 123",
        preco=350000,
        tipo="apartamento"
    )
    negociacao = Negociacao(
        cliente=cliente,
        imovel=imovel,
        valor_negociado=340000,
        tipo="Compra e venda"
    )

    print("\n--- Dados da negociação ---")
    print(negociacao)

    print("\n--- Conclusão ---")
    negociacao.concluir()
    print(f"Status: {negociacao.get_status()}")
    print(f"Contrato assinado: {negociacao.get_contrato().esta_assinado()}")
    print(f"Negociações do cliente: {len(cliente.get_negociacoes())}")


if __name__ == "__main__":
    main()
