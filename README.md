# Sistema de Gestão Imobiliária

Projeto escolar em Python para praticar Programação Orientada a Objetos (POO).

## Estrutura do projeto

- \`modelos_base.py\`: classe \`Imovel\`, com atributos privados, getters, setters e validações.
- \`modelos.py\`: classes \`Cliente\`, \`Negociacao\` e \`Contrato\`.
- \`main.py\`: demonstração de uso do sistema.
- \`testes.py\`: testes automatizados das classes.
- \`diagrama_uml.md\`: diagrama UML e explicação dos relacionamentos.

## Funcionalidades

- Representar imóveis com endereço, preço e tipo.
- Cadastrar clientes com nome, CPF e telefone.
- Criar negociações entre clientes e imóveis.
- Criar um contrato associado a cada negociação.
- Concluir uma negociação e assinar seu contrato.
- Cancelar negociações ainda não concluídas.
- Validar os dados informados.
- Testar os comportamentos com a biblioteca padrão \`unittest\`.

## Validações

- Endereço deve ser um texto com pelo menos 5 caracteres.
- Preço do imóvel e valor negociado devem ser maiores que zero.
- Tipo de imóvel deve ser \`casa\`, \`apartamento\`, \`terreno\`, \`comercial\` ou \`chacara\`.
- Cliente precisa ter nome, CPF e telefone informados.
- Quando um dado inválido é enviado aos setters de \`Imovel\`, o valor anterior é mantido.

## Como executar

É necessário ter Python 3 instalado. Abra o terminal nesta pasta e execute:

\`\`\`bash
python main.py
\`\`\`

No Windows, se necessário, use:

\`\`\`bash
py main.py
\`\`\`

## Como executar os testes

\`\`\`bash
python -m unittest -v testes.py
\`\`\`

No Windows, se necessário:

\`\`\`bash
py -m unittest -v testes.py
\`\`\`

## Conceitos de POO demonstrados

- **Encapsulamento:** atributos privados iniciados com \`__\`.
- **Abstração:** classes que representam entidades do domínio imobiliário.
- **Associação:** cliente relacionado às suas negociações.
- **Agregação:** negociação referencia um imóvel que existe independentemente dela.
- **Composição:** cada negociação cria e mantém seu contrato.
