def analisar_lista(lista_numeros):
  
    media = sum(lista_numeros) / len(lista_numeros)
    maior = max(lista_numeros)
    menor = min(lista_numeros)
    pares = sum(1 for num in lista_numeros if num % 2 == 0)
    
    return {'media': media, 'maior': maior, 'menor': menor, 'pares': pares}

numeros = [10, 23, 5, 8, 12, 33, 42, 7, 19, 28, 3, 16, 9, 50, 21]

resultado = analisar_lista(numeros)

print(f"Média: {resultado['media']}")
print(f"Maior número: {resultado['maior']}")
print(f"Menor número: {resultado['menor']}")
print(f"Quantidade de números pares: {resultado['pares']}")
