"""
Módulo lista_segura
"""


def adicionar_item_lista_segura(lista_original, novo_item):
    nova_lista = lista_original.copy()
    nova_lista.append(novo_item)
    return nova_lista


if __name__ == "__main__":
    lista_frutas = ["maçã", "banana", "laranja"]
    lista_frutas_atualizada = adicionar_item_lista_segura(lista_frutas, "uva")

    print(f"Lista original: {lista_frutas}")
    print(f"Nova lista: {lista_frutas_atualizada}")
