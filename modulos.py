#import math (import genérico, importação do módulo completo)
import condicionais as cond #importacao de modulo criado
from math import sqrt #(importação de apenas uma função)

#from math import * #import universal, nesse caso tambem nao precisa usar math.funcao
#não é recomendado o import universal

#import math as m #uso de alias para uma bibioteca

print(sqrt(81)) #sqrt calcula a raiz quadrada
#print(math.sqrt(81)) #sqrt calcula a raiz quadrada

#convenção em python para que módulos importados nao sejam executados antes da hora, 
# o programa começa a rodar a partir daqui
if __name__ == '__main__':
    
