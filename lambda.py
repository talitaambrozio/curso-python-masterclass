#Funções Lambda (anônimas): são criadas e usadas na mesma hora, é tipo um atalho de função
#não possuem nome
#Sintaxe:
#lambda argumentos: expressao

#ex.: variável que se comporta como uma função
# quadrado = lambda x: x**2

# for i in range(1,11):
#     print(quadrado(i))
    
#exemplo -> verificando se é par
par = lambda x: x % 2 == 0
print(par(9))

