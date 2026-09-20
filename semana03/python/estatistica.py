"""
Módulo estatistica (bônus)
"""


def media(*valores):
    if not valores:
        return None
    return sum(valores) / len(valores)


def mediana(*valores):
    if not valores:
        return None

    valores_ordenados = sorted(valores)
    quantidade = len(valores_ordenados)
    meio = quantidade // 2

    if quantidade % 2 == 0:
        return (valores_ordenados[meio - 1] + valores_ordenados[meio]) / 2
    return valores_ordenados[meio]


def moda(*valores):
    if not valores:
        return None

    contagem = {}
    for valor in valores:
        contagem[valor] = contagem.get(valor, 0) + 1

    maior_frequencia = max(contagem.values())
    valores_moda = [valor for valor, frequencia in contagem.items() if frequencia == maior_frequencia]

    return valores_moda


if __name__ == "__main__":
    print("Testando o módulo estatistica:")
    print(f"Média: {media(2, 4, 6, 8):.2f}")
    print(f"Mediana: {mediana(2, 4, 6, 8)}")
    print(f"Moda: {moda(1, 2, 2, 3, 3, 3, 4)}")
