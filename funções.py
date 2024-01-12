#Bloco de código que realiza determinada tarefa
#benefícios: modularização, reuso de código e legibilidade
#para criar uma funcao usa-se a palavra chave reservada 'def'
#Sintaxe:
# def <nome_funcao> ([argumentos]):
#     <instrucoes

# def mensagem():
#     print('Primeira Função')
    
# mensagem()

# #Função com argumentos
# def somar(a,b):
#     print(a+b)

# somar(10,20)

# def multipiclar(x,y):
#     return x * y

# print(multipiclar(2,5))

# def dividir(x,y):
#     if y != 0:
#         return x/y
#     else:
#         print('Não é possível dividir por zero!') 

# if __name__ == '__main__':
#     a = int(input('Digite um número: '))
#     b = int(input('Digite outro número: '))
    
#     r = dividir(a,b)
    
def quadrado(val):
    quadrados = []
    for x in val:
        quadrados.append(x ** 2)
        return quadrados


if __name__ == '__main__':
    valores = [2,5,7,9,12]
    resultados = quadrado(valores)
    
    for g in resultados:
        print(g)
        
#passando parâmetros padrões: eles são inicializados com valores, se ninguem chamar a função passando um novo valor a eles,
#será considerado seu valor padrão, ex.:
def contar(num=11, caractere='+'):
    for i in range(1, num):
        print(caractere)   

#quando uma variável no parâmetro não possui valor padrão, ela se torna obrigatória, e tem prioridade na ordem:
def conta(caractere, num=11):
        for i in range(1, num):
            print(caractere) 
            
        
if __name__ == '__main__':
    #contar() usando parametro padrao
    #contar(num=5,caractere='&') #escrever o nome dos parâmetros é opcional:
    contar(5,'&')
    #na hora de chamar a função, se os parâmetros estiverem nomeados a ordem nao importa:
    contar(num=6, caractere='+')
    


               