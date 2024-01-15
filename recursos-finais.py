#Trocando valores entre duas variáveis

var1 = 12
var2 = 31

var2, var1 = var1, var2

print(f'var2: {var1}, var2: {var2}')

#Operador Ternário
menor = var1 if var1 < var2 else var2
print(f'Menor valor é {menor}')

#Generators
valores = [1,3,5,7,9,11,13,15]
quadrados = (item**2 for item in valores)
#diferente da compreensao de listas, os generators vao calcular os quadrados
#aos poucos, conforme forem solicitado, nao sobrecarregando a memoria
print(quadrados)
for valor in quadrados:
    print(valor)
    
#Enumerate
bebidas = ['Café', 'Chá', 'Água', 'Suco']
for i, item in enumerate(bebidas):
    print(f'Índice: {i}, Item: {item}')
    
#Outra forma de usar try catch mais encurtada

with open('frutas.dat', 'r', encoding='utf-8') as a:
    for linha in a:
        print(linha)    
#essas 3 linhas fazem tudo que o bloco try, catch exception fazem, mas resumidas, ao usar 
#o with junto do open, nao é necessário fechar com close() pois ele já está embutido        