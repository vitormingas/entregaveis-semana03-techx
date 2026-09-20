"""
Script Principal - Sprint 3
"""

import calculadora
import utilidades
from lista_segura import adicionar_item_lista_segura


def main():
    print("===== Demonstração do módulo calculadora =====")
    print(f"Soma: {calculadora.somar(10, 5)}")
    print(f"Subtração: {calculadora.subtrair(10, 5)}")
    print(f"Multiplicação: {calculadora.multiplicar(10, 5)}")
    print(f"Divisão: {calculadora.dividir(10, 5)}")
    print(f"Divisão por zero: {calculadora.dividir(10, 0)}")

    print("\n===== Demonstração do módulo utilidades =====")
    temperatura_convertida = utilidades.converter_temperatura(100, "C", "F")
    print(f"100°C em Fahrenheit: {temperatura_convertida:.2f}")

    senha_valida = utilidades.validar_senha("Senha@123")
    print(f"A senha 'Senha@123' é válida? {senha_valida}")

    total_compra = utilidades.caixa(15.90, 8.50, 22.00)
    print(f"Total da compra: R$ {total_compra:.2f}")

    utilidades.ficha_aluno(nome="João", idade=21, curso="Ciência da Computação")

    print("\n===== Demonstração da lista segura =====")
    lista_original = [1, 2, 3]
    lista_atualizada = adicionar_item_lista_segura(lista_original, 4)
    print(f"Lista original (inalterada): {lista_original}")
    print(f"Lista atualizada: {lista_atualizada}")


if __name__ == "__main__":
    main()
