# numero = 1

# while(numero <= 10):
#     print(numero)
#     numero += 1
# print('Laço encerrado.')

#para casos em que sabemos quantas vezes o laço irá executar

nome = None

while True:
    print('Digite seu nome, ou x para encerrar: ')
    nome = input()
    if (nome == 'x' or nome == 'X'):
        break
    print(f'Bem vindo, {nome}')
    
print('Até logo!')