import random


# print('Gerar cinco números inteiros aleatórios entre 1 e 50: \n')
# for i in range(5):
#     n = random.randint(1,50)
#     print(f'Número gerado: {n}')
    
#gerando números flutuantes aleatórios
valor = random.random()
print(valor)

#obs: se quiser especificar um limite para o flutuante basta multiplicar pelo número, ex.:
print(f'Número gerado: {valor * 10}')

#para arrendondar o resultado usar o round e definir casas decimais:
print(f'Número gerado: {round(valor * 10, 2)}')

#é possível gerar numeros flutuantes aleatórios usando o uniform, com ele não é necessário
#multiplicar para ajustar a escala:
valor = random.uniform(1,100)
print(f'Número: {round(valor, 2)}')

#escolhendo um numero aleatorio de uma lista
L = [1,6,7,5,8,9]
n = random.choice(L)
print(f'Número escolhido: {n}')

#pegando uma amostra de uma lista
m = random.sample(L, 3) #pega 3 numeros da lista L
print(f'Números escolhidos: {m}')

#Embaralhar lista
print(f'Exibir lista orignal: {L}')
print(f'Embaralhar lista e exibí-la:')
listaEmb = random.shuffle(L)
print(L)
    