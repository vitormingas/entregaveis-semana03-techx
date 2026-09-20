"""
bonus_extra (bônus)
"""

import estatistica as est


def fatorial(numero):
    if numero < 0:
        print("Erro: fatorial não é definido para números negativos.")
        return None
    if numero in (0, 1):
        return 1
    return numero * fatorial(numero - 1)


def relatorio(titulo, *linhas, **config):
    separador = config.get("separador", "-")
    usar_maiusculas = config.get("maiusculas", False)

    titulo_exibido = titulo.upper() if usar_maiusculas else titulo

    print(titulo_exibido)
    print(separador * len(titulo_exibido))
    for linha in linhas:
        print(f"- {linha}")


if __name__ == "__main__":
    print("===== Bônus: módulo estatistica importado com alias 'est' =====")
    print(f"Média: {est.media(5, 10, 15):.2f}")
    print(f"Mediana: {est.mediana(5, 10, 15)}")
    print(f"Moda: {est.moda(1, 1, 2, 3)}")

    print("\n===== Bônus: fatorial recursivo =====")
    print(f"Fatorial de 5: {fatorial(5)}")

    print("\n===== Bônus: relatório dinâmico =====")
    relatorio(
        "Relatório de Vendas",
        "Produto A: 10 unidades",
        "Produto B: 5 unidades",
        separador="=",
        maiusculas=True,
    )
