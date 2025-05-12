# -*- coding: utf-8 -*-


def analisar_lista(numeros):
    if not numeros:
        return "Lista vazia."

    media = sum(numeros) / len(numeros)
    maior = max(numeros)
    menor = min(numeros)
    pares = len([n for n in numeros if n % 2 == 0])

    return {
        "media": round(media, 2),
        "maior": maior,
        "menor": menor,
        "pares": pares
    }
