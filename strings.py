#uma string é uma sequência de caracteres, são imutáveis
nome = 'Talita'
letra = nome[2]
print(letra)
print(len(nome))

#separando uma frase com split através dos espaços
frase = 'Esta é uma frase pequena.'
palavras = frase.split()
print(palavras)

for palavra in palavras:
    print(palavra)
    
#buscando caracteres em uma string
# email = input('Digite seu email: ')
# arroba = email.find('@')
# print(arroba)
#obs: quando o método find retorna -1 é porque não encontrou o valor procurado
#separando o nome do usuário do nome do domínio do email
# usuario = email[0:arroba]
# domínio = email[arroba+1:]
# print(usuario)
# print(domínio)

#deixando caracteres maíusculos
sobrenome = 'ambrozio santos'
print(sobrenome.upper())

#deixando caracteres minúsculos
print(sobrenome.lower())

#deixando apenas a 1ª letra da frase em maiúsculo
print(sobrenome.capitalize())

#deixando todas as 1ª letras de cada palavra de frase em maiúsculo
print(sobrenome.title())

#substituindo partes de uma string em uma nova string
suplemento = 'cloreto de magnésio'
n_suplemento = suplemento.replace('magnésio', 'zinco')
print(suplemento)
print(n_suplemento)

#Removendo espaços em branco
frase = '             Essa é uma frase'
print(frase.lstrip()) #elimina espaço da esquerda
print(frase.rstrip()) #elimina espaço da direita
print(frase.strip()) #elimina espaços da esqueda e direita

#justificando uma frase
fruta = 'Abacate'
print(fruta)
print(fruta.rjust(20)) #alinha à direita
print(fruta.ljust(20, '-')) #alinha à esquerda e preenche com caracter à direita
print(fruta.center(20))
#obs: o rjust e ljust aceita preenchimento com caracteres, só passar no segundo parâmetro

#Verificação de sufixo e prefixo - função booleana
p = 'Talita Ambrozio'
print(p.startswith('T'))
print(p.endswith('T'))

#Documentando em python - usar 3 aspas duplas
"""
Docstrings: Aqui você insere a documentação do seu código
"""