#Sintaxe: nome_lista = [valores]

# notas = [5,7,8,6,9]

n1 = [1,6,5,8,9]
n2 = [1,8,78,98,45,99]

valores = n1 + n2 #faz a concatenação da lista n1 e n2
# print(valores)

#acessando índices da lista
# print(valores[0])

#para alterar o valor de um índice:
# valores[0] = 100
# print(valores[0])

#imprimindo uma sequencia de valores da lista com o slice
# print(valores[0:2]) #vai imprimir a partir da posicao zero 2 valores
#obs: se não colocar nada antes dos dois pontos o python entende que é
#para acessar a partir do início da lista, e se não colocar nada após os dois pontos
#ele entende que é para acessar até o fim da lista

#para saber quantos elementos contém uma lista
# print(len(valores))
# print(sorted(valores)) #imprime a lista em ordem crescente
# print(sorted(valores, reverse=True)) #imprime a lista em ordem decrescente
# print(sum(valores)) #soma todos os elementos da lista
# print(min(valores)) #retorna o valor mínimo da lista
# print(max(valores)) #retorna o valor máximo da lista

#método para inserir item no final da lista: append

valores.append(13) #insere no fim da lista
print(valores)

valores.pop() #remove o último elemento da lista
valores.pop(3) #remove o elemento da posição 3 da lista
print(valores)
valores.insert(3,999) #na posição 3 insere o elemento 999
print(valores)
print(12 in valores) #verifica se o valor 12 consta na lista

#formas de criar uma lista vazia:

#planetas = []
#planetas = list()

planetas = ['Mercúrio', 'Vênus', 'Marte', 'Saturno', 'Urano', 'Netuno']
for planeta in planetas:
    print(planeta)
