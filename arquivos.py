#Manipulação de arquivos de texto

#Lendo o conteúdo de um arquivo


# print(f'\nMétodo read():\n')
# print(manipulador.read())

# print(f'\nMétodo readline():\n')
# print(manipulador.readline())

# print(f'\nMétodo readlines():\n')
# print(manipulador.readlines())

# try: 
#     #Acessando arquivo dentro do mesmo diretório:
#     #manipulador = open('arquivo.txt', 'r', encoding='utf-8')
#     #acessando arquivo de outros diretórios:
#     manipulador = open('C:\\Teste\\Dados 8.txt', 'r', encoding='utf-8')
#     for linha in manipulador:
#         linha = linha.rstrip()
#         print(linha)
# except IOError:
#     print(f'Não foi possível abrir o arquivo.')
# else:
#     manipulador.close()
    
#obs: sempre fechar o manipulador do arquivo para liberar espaço 

#buscar termos dentro de arquivo

# texto = input('Qual termo deseja procurar no arquivo? ')
# try: 
#     manipulador = open('arquivo.txt', 'r', encoding='utf-8')
#     for linha in manipulador:
#         linha = linha.rstrip()
#         if texto in linha:
#             print(linha)
#         else:
#             print(f'String não encontrada!')
#             break
# except IOError:
#     print(f'Não foi possível abrir o arquivo.')
# else:
#     manipulador.close()
    
#Gravando dados em um arquivo de texto

# try: 
#     # manipulador = open('arquivo.txt', 'w', encoding='utf-8')
#     # manipulador.write('Teste dados novos.')
#     #obs: o write() grava dados no arquivo mas substituindo o que já existe nele.
#     #para apenas adicionar novos dados sem perder os antigos usar o append a:
#     manipulador = open('arquivo.txt', 'a', encoding='utf-8')
#     manipulador.write('\nTeste dados novos acrescentados.\n')
#     #para gravar a partir de uma lista de dados usar o writelines
# except IOError:
#     print(f'Não foi possível abrir o arquivo.')
# else:
#     manipulador.close()

frutas = ['Morango\n', 'Mamao\n', 'Melao\n']
try: 
    # manipulador = open('arquivo.txt', 'w', encoding='utf-8')
    # manipulador.write('Teste dados novos.')
    #obs: o write() grava dados no arquivo mas substituindo o que já existe nele.
    #para apenas adicionar novos dados sem perder os antigos usar o append a:
    manipulador = open('frutas.dat', 'w', encoding='utf-8')
    manipulador.writelines(frutas)
    
except IOError:
    print(f'Não foi possível abrir o arquivo.')
else:
    manipulador.close()
    
