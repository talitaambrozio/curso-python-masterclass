#Coleções não ordenadas de valores únicos

planeta_anao = {'Plutao', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(len(planeta_anao))

#verificar se um elemento consta no set
print('Lua' in planeta_anao)

for astro in planeta_anao:
    print(astro.upper())
    
#criando um set a partir de uma lista
lista_astros = ['Plutao', 'Ceres', 'Eris', 'Haumea', 'Makemake','Makemake']
astro_set = set(lista_astros)
print(astro_set)

#Comparação entre conjuntos
astros1 = {'Plutao', 'Ceres', 'Eris', 'Haumea', 'Makemake','Makemake'}
astros2 = {'Plutao', 'Ceres', 'Eris', 'Haumea', 'Makemake','Makemake2'}
print(astros1 == astros2)

#Junção de conjuntos
print(astros1 | astros2)
#ou
print(astros1.union(astros2))

#Intersecção de Conjuntos
print(astros1 & astros2)
print(astros1.intersection(astros2))

#Diferença entre conjuntos
print(astros1 ^ astros2)
print(astros1.symmetric_difference(astros2))

#Adicionando elementos no set
astros1.add('Urano')
astros1.add('Sol')
print(astros1)

#removendo elementos
astros1.remove('Urano')
#também é possível remover elemento com o discard, com ele caso o elemento nao existe nao ocorre erro
astros1.discard('terra')
astros1.pop() #remove um elemento aleatório do set
astro.clear() #remove os elementos do set