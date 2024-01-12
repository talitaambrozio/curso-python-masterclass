#permite aplicar outra funcao a cada elemento de um objeto iterável
#é uma função que aplica funções, pode usar uma funcao normal ou uma lambda
#Sintaxe
#map(funcao, iterável)

#multiplicar cada valor de uma lista por 2

num = [1,2,3,4,5,6,7,8]
dobro = list(map(lambda x: x * 2, num))
print(dobro)

palavras = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']
maiusculas = list(map(str.upper, palavras))
print(maiusculas)

