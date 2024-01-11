bebidasFavoritas = []

while True:
    print('Digite uma bebida favorita ou digite \'x\' para encerrar: ')
    bebida = input()
    
    if (bebida == 'x' or bebida == 'X'):
        break
    else:
        bebidasFavoritas.append(bebida)
bebidasFavoritas.sort() #ordena a lista original em ordem crescente/alfabetica
print(bebidasFavoritas)