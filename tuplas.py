#São imutáveis

tupla = (2,45,6,8,45,1)
print(tupla)

halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
t1 = (5,6,6,6,8,5,9,8,7,4,6,0)

print(t1.count(6)) #retorna quantidade de repetições do numero 6

print(halogenios[0:2]) #mesma funcao da lista, imprime a partir do 0 até o 2
print(halogenios[-2:]) #imprime a partir do penúltimo elemento até o final
print('Cl' in halogenios)

#Operações não disponíves na tupla: tudo que altera uma lista

#É possível criar uma tupla a partir de uma lista
lista1 = ['F', 'Cl', 'Br', 'I', 'At']
elementos = tuple(lista1)
print('Tipo lista', type(elementos), elementos)