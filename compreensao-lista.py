numeros = [1,4,7,9,10,12,21]

quadrados = [num**2 for num in numeros]

print(quadrados)

#Criar uma lista de numeros pares de 0 a 10
pares = [num for num in range(11) if num % 2 == 0]

print(pares)

#contar a quantidade de vogais dentro de um texto
frase = 'A lógica é apenas o princípio da sabedoria e não o seu fim'
vogais = ['a', 'e', 'i', 'o', 'u', 'á', 'é','í', 'ó', 'ú']

lista_vogais = [v for v in frase if v in vogais]
print(f'A frase possui {len(lista_vogais)} vogais.')
print(lista_vogais)