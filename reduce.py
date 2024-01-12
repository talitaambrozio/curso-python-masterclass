#realiza operações cumulativas em sequencias de elementos, ela acumula valores na sequencia e
#retorna um unico valor, sendo o valor total
#Sintaxe
#reduce(funcao, sequencia, valor_inicial)

from functools import reduce

def mult(x, y):
    return x * y

numeros = [1,2,3,4,5,6]

resultado_multiplicacao_cumulativo = reduce(mult, numeros)
print(resultado_multiplicacao_cumulativo)