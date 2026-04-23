# Explicação técnica do código `num_primos.py`

Este arquivo explica a estrutura e os princípios de design do código de verificação de números primos.

## Objetivo

A função `is_prime(n)` determina se um inteiro é primo, usando uma implementação clara, modular e eficiente.

## Organização do código

### `is_prime(n: int) -> bool`

- Valida que a entrada seja um inteiro.
- Trata casos especiais de forma explícita:
  - `n <= 1` retorna `False`.
  - `n == 2` e `n == 3` retornam `True`.
- Elimina rapidamente múltiplos de `2` e `3`.
- Encaminha a verificação de divisores maiores para uma função auxiliar.

### `_has_no_six_step_divisors(number: int, start: int) -> bool`

- Faz a verificação principal de divisores possíveis.
- Trabalha com passos de `6` em `6` para testar apenas os candidatos `6k - 1` e `6k + 1`.
- Continua até `start * start <= number`, o que é suficiente para determinar primalidade.

### `main()`

- Agrupa a lógica de execução interativa em uma única função.
- Permite usar o módulo como biblioteca sem executar o código de entrada/saída automaticamente.

## Por que isso é Clean Code?

- Funções pequenas e com responsabilidade única.
- Nomes descritivos e consistentes.
- Separação entre lógica de verificação e interface com o usuário.
- Tratamento explícito de tipos inválidos.

## Fluxo de execução

Quando o arquivo é executado diretamente:

```python
if __name__ == "__main__":
    main()
```

O `main()` lê um número do usuário, chama `is_prime(valor)` e imprime o resultado.

## Benefícios do algoritmo

- Evita testes desnecessários com números pares e múltiplos de 3.
- Limita a busca de divisores até a raiz quadrada do número.
- Usa um padrão conhecido para números primos maiores que 3: `6k ± 1`.

## Conclusão

A versão atual do código é mais legível e modular, mantendo a eficiência da verificação de primalidade. Isso facilita manutenção e reutilização em outros módulos ou testes.
