#Sintaxe
#print(objetos, argumentos)

#pode usar aspas simples ou duplas
#por padrão a função print coloca uma quebra de linha no fim da impressão,
#é possível desabilitar essa quebra de linha usando o comando end='':

print('Imprime a mensagem e muda de linha')
print('Imprime a mensagem e permanece na linha', end='')

mensagem = 'Função print()'
print(mensagem)
print('Texto Literal')

#Elementos posicionais
nome = 'Talita Ambrozio'
varialvelNome = 'Nome'
print('Nome -', nome)
print(varialvelNome, '-', nome )

#Concatenação
nomeInput = input('Digite seu nome: ')
print('Olá, ' + nome + "! Bem vindo ao curso de Python!")

#Formatando mensagens
cidade = 'Bauru'
idade = 29
msg_formatada = 'O nome dela é {0}, ela é de {1} e tem {2} anos'.format(nome, cidade, idade)
print(msg_formatada)

#forma mais fácil de formatar
msg_formatada_atualizada = f'Olá, meu nome é {nome}, sou de {cidade} e tenho {idade} anos'
print(msg_formatada_atualizada)

#Operações com f string
a = 10
b = 5
res = f'A soma de {a} com {b} é igual a {a+b}'
print(res)

#Formatando casas decimais
valor = 125.79898
print(f'O valor é {valor:.2f}')

#Caracteres de Escape
#alguns caracteres causam erro no python, por exemplo quando for imprimir aspas dentro do print
#para resolver esse problemas podemos usar a barra invertida antes do caractere que causaria 
#problema
#exemplo:
print('Ola, \'Mundo\'')

#Usando tabulação
print(f'Nome: {nome}\tIdade: {idade}')