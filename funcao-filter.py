#filtra elementos de uma sequencia de acordo com os criterios estabelecidos
#Sintaxe
#filter(funcao, sequencia)

def numeros_pares(n):
    return n % 2 == 0

numeros = [1,2,3,4,5,6,7,8,9,10]

#obs: o nome da funcao dentro do parametro do filter vai sem os parenteses
num_pares = list(filter(numeros_pares, numeros))
print(num_pares)

num_impar = list(filter(lambda x: x % 2 != 0, numeros))
print(num_impar)