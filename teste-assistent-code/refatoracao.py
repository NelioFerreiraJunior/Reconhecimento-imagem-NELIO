from typing import Sequence, Tuple


def calcular_estatisticas(numeros: Sequence[float]) -> Tuple[float, float, float, float]:
    """Retorna a soma, media, maior e menor valor da lista de numeros."""
    if not numeros:
        raise ValueError("A lista de numeros nao pode estar vazia.")

    total = sum(numeros)
    media = total / len(numeros)
    maior = max(numeros)
    menor = min(numeros)

    return total, media, maior, menor


def main() -> None:
    numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    total, media, maior, menor = calcular_estatisticas(numeros)

    print(f"total: {total}")
    print(f"media: {media}")
    print(f"maior: {maior}")
    print(f"menor: {menor}")


if __name__ == "__main__":
    main()
