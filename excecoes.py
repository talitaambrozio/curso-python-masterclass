#Exceção: objeto que representa um erro durante a execução do programa
#para fazer o tratamento usa-se o bloco try...except

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

try:
    #nesse bloco colocar a lógica a ser executada e que pode ocasionar uma execao
    r = round(n1/n2, 2)
except ZeroDivisionError:
    #nesse bloco capturar a excecao
    print('Não é possível dividir por zero!')    
#obs: é possível colocar só o except sem especificar uma exceção    
else:  
    #é opcional, nesse bloco colocar o resultado da logica caso nao ocorra erros na execucao 
    print(f'Resultado: {r}')
