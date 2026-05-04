# Projeto de Exemplos em Python

Este projeto contém exemplos simples de scripts Python e explicações associadas para aprender conceitos básicos como:

- operações matemáticas e formatação de saída
- verificação de números primos
- cálculo de estatísticas básicas
- análise de código e depuração

## Estrutura do projeto

- `debug.py` - cálculo de valor total de itens comprados com imposto e desconto
- `num_primos.py` - verificação interativa de número primo
- `refatoracao.py` - cálculo de soma, média, maior e menor valor em uma lista
- `explicacao-debug.md` - análise de problemas encontrados e correções para `debug.py`
- `explicacao_num_primo.md` - explicação técnica do algoritmo de verificação de primos
- `explicacao_refatoracao.md` - explicação e refatoração do código de estatísticas

## Descrições dos arquivos

### `debug.py`

Este script solicita ao usuário:

- nome do cliente
- quantidade e preço de três itens
- percentual de desconto de cupom (ou 0)

Ele calcula:

- total de cada item
- subtotal
- imposto de 10%
- desconto baseado no cupom
- total final formatado como recibo

### `num_primos.py`

Script interativo para verificar se um número inteiro é primo.

Funções principais:

- `is_prime(n: int) -> bool`: valida a entrada e verifica primalidade
- `_has_no_six_step_divisors(number: int, start: int) -> bool`: verifica divisores potenciais usando o passo `6k ± 1`

### `refatoracao.py`

Implementa cálculo de estatísticas básicas para uma lista de números:

- soma total
- média
- maior valor
- menor valor

A função `calcular_estatisticas(numeros: Sequence[float]) -> Tuple[float, float, float, float]` retorna todos esses valores de forma clara e reutilizável.

## Como executar

Execute os scripts usando Python 3 a partir do diretório do projeto:

```bash
python debug.py
python num_primos.py
python refatoracao.py
```

> Observação: o código assume que o terminal aceita entrada padrão e saídas formatadas.

## Requisitos

- Python 3.x

## Aprendizado e documentação

Os arquivos `explicacao-debug.md`, `explicacao_num_primo.md` e `explicacao_refatoracao.md` oferecem explicações detalhadas sobre:

- erros comuns em Python
- lógica de primalidade
- boas práticas de refatoração e nomes de variáveis

## Sugestões de melhorias

- adicionar validação de entrada mais robusta em `debug.py`
- tornar `num_primos.py` compatível com múltiplas consultas sem reiniciar o programa
- permitir entrada de listas no `refatoracao.py` em vez de usar valores fixos
