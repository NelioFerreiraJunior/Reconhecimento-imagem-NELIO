def is_prime(n: int) -> bool:
    """Verifica se um inteiro é primo.

    Retorna True para números primos e False para os demais.
    """
    if not isinstance(n, int):
        raise TypeError("O valor deve ser um inteiro")

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    return _has_no_six_step_divisors(n, start=5)


def _has_no_six_step_divisors(number: int, start: int) -> bool:
    """Verifica divisores potenciais do número usando passos de 6 em 6."""
    while start * start <= number:
        if number % start == 0 or number % (start + 2) == 0:
            return False
        start += 6
    return True


def main() -> None:
    """Executa o programa interativo de verificação de primo."""
    valor = int(input("Digite um número para verificar se é primo: "))
    if is_prime(valor):
        print(f"{valor} é primo.")
    else:
        print(f"{valor} não é primo.")


if __name__ == "__main__":
    main()
