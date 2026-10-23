# Sistema de Gestão Imobiliária

Projeto escolar em Python para praticar Programação Orientada a Objetos (POO).

## Arquivo principal

- `modelos_base.py`: classe `Imovel`, com atributos privados, construtor, getters, setters e validação dos dados.

## Validações implementadas

- O endereço deve ser um texto com pelo menos 5 caracteres.
- O preço deve ser numérico e maior que zero.
- O tipo deve ser `casa`, `apartamento`, `terreno`, `comercial` ou `chacara`.
- Quando um dado inválido é informado, o valor anterior é mantido.

## Como executar

No terminal do VS Code, dentro desta pasta, execute:

```bash
python modelos_base.py
```

No Windows, se o comando acima não funcionar, tente:

```bash
py modelos_base.py
```
