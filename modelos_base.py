class Imovel:
    """Classe base para representar um imóvel."""

    TIPOS_VALIDOS = {
        "casa",
        "apartamento",
        "terreno",
        "comercial",
        "chacara"
    }

    def __init__(self, endereco, preco, tipo):
        # Valores iniciais seguros; os setters validam os dados recebidos.
        self.__endereco = "Endereço não informado"
        self.__preco = 0.0
        self.__tipo = "casa"

        self.set_endereco(endereco)
        self.set_preco(preco)
        self.set_tipo(tipo)

    # Getters
    def get_endereco(self):
        return self.__endereco

    def get_preco(self):
        return self.__preco

    def get_tipo(self):
        return self.__tipo

    # Setters com validação
    def set_endereco(self, endereco):
        if isinstance(endereco, str) and len(endereco.strip()) >= 5:
            self.__endereco = endereco.strip()
        else:
            print("ERRO: endereço inválido. O valor anterior foi mantido.")

    def set_preco(self, preco):
        if (
            isinstance(preco, (int, float))
            and not isinstance(preco, bool)
            and preco > 0
        ):
            self.__preco = float(preco)
        else:
            print("ERRO: o preço deve ser um número maior que zero. "
                  "O valor anterior foi mantido.")

    def set_tipo(self, tipo):
        if (
            isinstance(tipo, str)
            and tipo.strip().lower() in self.TIPOS_VALIDOS
        ):
            self.__tipo = tipo.strip().lower()
        else:
            print("ERRO: tipo inválido. Use casa, apartamento, terreno, "
                  "comercial ou chacara. O valor anterior foi mantido.")

    def __str__(self):
        return (
            f"Endereço: {self.get_endereco()}\n"
            f"Preço: R$ {self.get_preco():,.2f}\n"
            f"Tipo: {self.get_tipo()}"
        )


if __name__ == "__main__":
    print("=== TESTE DA CLASSE IMOVEL ===")

    imovel = Imovel(
        endereco="Rua das Flores, 123",
        preco=350000,
        tipo="apartamento"
    )
    print(imovel)

    # Testes de validação: valores inválidos não substituem os válidos.
    imovel.set_endereco("abc")
    imovel.set_preco(-100)
    imovel.set_tipo("castelo")

    assert imovel.get_endereco() == "Rua das Flores, 123"
    assert imovel.get_preco() == 350000.0
    assert imovel.get_tipo() == "apartamento"

    print("\nTodos os testes foram executados com sucesso!")
