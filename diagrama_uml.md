# Diagrama UML — Sistema de Gestão Imobiliária

O diagrama representa as quatro classes principais e seus relacionamentos.

\`\`\`mermaid
classDiagram
    class Cliente {
        -str nome
        -str cpf
        -str telefone
        -list negociacoes
        +get_nome()
        +get_cpf()
        +get_telefone()
        +get_negociacoes()
        +adicionar_negociacao(negociacao)
    }

    class Imovel {
        -str endereco
        -float preco
        -str tipo
        +get_endereco()
        +get_preco()
        +get_tipo()
        +set_endereco(endereco)
        +set_preco(preco)
        +set_tipo(tipo)
    }

    class Negociacao {
        -Cliente cliente
        -Imovel imovel
        -float valor_negociado
        -str status
        -Contrato contrato
        +get_cliente()
        +get_imovel()
        +get_contrato()
        +concluir()
        +cancelar()
    }

    class Contrato {
        -float valor
        -str tipo
        -date data_assinatura
        -bool assinado
        +get_valor()
        +get_tipo()
        +esta_assinado()
        +assinar()
    }

    Cliente "1" --> "0..*" Negociacao : participa
    Negociacao "0..*" o-- "1" Imovel : referencia
    Negociacao "1" *-- "1" Contrato : possui
\`\`\`

## Significado dos relacionamentos

- **Associação:** um cliente pode participar de nenhuma ou várias negociações; cada negociação tem um cliente.
- **Agregação:** a negociação referencia um imóvel que pode continuar existindo independentemente dela.
- **Composição:** o contrato é criado e gerenciado pela negociação.

## Conceitos de POO

- **Encapsulamento:** atributos privados com prefixo \`__\` e métodos de acesso.
- **Abstração:** cada classe representa uma entidade do domínio imobiliário.
- **Associação entre objetos:** \`Negociacao\` trabalha com instâncias de \`Cliente\` e \`Imovel\`.
- **Composição:** cada negociação cria seu próprio objeto \`Contrato\`.
