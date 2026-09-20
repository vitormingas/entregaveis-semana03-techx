"""
Módulo utilidades
"""


def converter_temperatura(valor, escala_origem, escala_destino):
    escala_origem = escala_origem.upper()
    escala_destino = escala_destino.upper()

    if escala_origem == "C":
        valor_celsius = valor
    elif escala_origem == "F":
        valor_celsius = (valor - 32) * 5 / 9
    elif escala_origem == "K":
        valor_celsius = valor - 273.15
    else:
        print("Erro: escala de origem inválida.")
        return None

    if escala_destino == "C":
        return valor_celsius
    elif escala_destino == "F":
        return valor_celsius * 9 / 5 + 32
    elif escala_destino == "K":
        return valor_celsius + 273.15
    else:
        print("Erro: escala de destino inválida.")
        return None


def validar_senha(senha):
    caracteres_especiais = "!@#$%^&*()-_=+"

    tem_tamanho_minimo = len(senha) >= 8
    tem_maiuscula = any(caractere.isupper() for caractere in senha)
    tem_minuscula = any(caractere.islower() for caractere in senha)
    tem_digito = any(caractere.isdigit() for caractere in senha)
    tem_especial = any(caractere in caracteres_especiais for caractere in senha)

    return tem_tamanho_minimo and tem_maiuscula and tem_minuscula and tem_digito and tem_especial


def caixa(*precos):
    return sum(precos)


def ficha_aluno(**dados): 
    print("===== Ficha do Aluno =====")
    for chave, valor in dados.items():
        print(f"{chave.capitalize()}: {valor}")


if __name__ == "__main__":
    print("Testando o módulo utilidades:")

    print(f"25°C em Fahrenheit: {converter_temperatura(25, 'C', 'F'):.2f}")
    print(f"98.6°F em Celsius: {converter_temperatura(98.6, 'F', 'C'):.2f}")

    print(f"Senha 'abc123' é válida? {validar_senha('abc123')}")
    print(f"Senha 'Abc123!@' é válida? {validar_senha('Abc123!@')}")

    print(f"Total do caixa: R$ {caixa(10.5, 20, 5.25):.2f}")

    ficha_aluno(nome="Maria", idade=19, curso="Análise e Desenvolvimento de Sistemas")
