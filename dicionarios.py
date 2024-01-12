#Dicionários: permitem armazenar dados em pares de chave e valor
#não permite itens duplicados
#aceita itens de qualquer tipo

elemento = {
    'Z': 3,
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}
print(elemento)

print(f'Elemento: {elemento['nome']}')
print(f'O dicionário possui {len(elemento)} elementos.')

#Atualizar elementos do dicionário
elemento['grupo'] = 'Alcalinos'
print(elemento)

#Adicionar um elemento
elemento['periodo'] = 1
print(elemento)

#Exclusão de itens em dicionários
# del elemento['periodo']
# print(elemento)

#apagando todos os itens do dicionário
# elemento.clear()
# print(elemento)

#excluindo o dicionário da memória
# del elemento
# print(elemento) #erro pois ele nao existe mais

print(elemento.items())

for i in elemento.items():
    print(i)

print(elemento.keys())
for i in elemento.keys():
    print(i)

print(elemento.values())
for i in elemento.values():
    print(i)
    
#imprimindo o dicionario em forma de tabelinha
for i,j in elemento.items():
    print(f'{i}: {j}')