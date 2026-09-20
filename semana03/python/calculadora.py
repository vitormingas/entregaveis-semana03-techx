"""
Módulo calculadora
"""


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        print("Erro: não é possível dividir por zero.")
        return None
    return a / b


if __name__ == "__main__":
    print("Testando o módulo calculadora:")
    print(f"5 + 3 = {somar(5, 3)}")
    print(f"5 - 3 = {subtrair(5, 3)}")
    print(f"5 * 3 = {multiplicar(5, 3)}")
    print(f"5 / 3 = {dividir(5, 3):.2f}")
    print(f"5 / 0 = {dividir(5, 0)}")
