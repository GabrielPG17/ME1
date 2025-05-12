def analisar_lista(lista_numeros):
  
    media = sum(lista_numeros) / len(lista_numeros)
    maior = max(lista_numeros)
    menor = min(lista_numeros)
    pares = sum(1 for num in lista_numeros if num % 2 == 0)
    
    return {'media': media, 'maior': maior, 'menor': menor, 'pares': pares}

numeros = [analisar_lista]

resultado = analisar_lista(numeros)

print(f"Média: {resultado['media']}")
print(f"Maior número: {resultado['maior']}")
print(f"Menor número: {resultado['menor']}")
print(f"Quantidade de números pares: {resultado['pares']}")
