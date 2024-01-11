lista =  [2,6,9,4,0,12,3,7]
palavra = 'Talita'

for item in lista:
    print(item)

for letra in palavra:
    print(letra)
    
#Função range pode receber até 3 parâmetros, ex.: range(valor_inicial, valor_final, incremento)
#função range permite iterar dentro de um limite de numeros, passando por parametro o início e fim
#ou passando apenas o limite

for numero in range(1,10):
    print(numero)
    
#imprimindo várias vezes uma variável conforme quantidade definida no range()
nome = input('Digite seu nome: ')
for x in range(10):
    print(f'{x+1} {nome}')
    
#range(valor_inicial, valor_final, incremento)
for x in range(2, 20,2):
    print(x)
    
pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Safira', 'Diamante', 'Turmalina')

for pedra in pedras:
    if pedra == 'Quartzo':
        continue
    #continue encerra a iteração do laço, nesse caso será impresso todas as pedras menos o Quartzo
    print(pedra)