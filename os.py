#modulo os python: para gerenciar pastas e arquivos do sistema operacional
#outra opcao de biblioteca para esse gerenciamento é a pathlib ou shutil

#renomeando nome de arquivos em massa:
import os

os.chdir('C:\\Teste')
print(f'Diretório atual: {os.getcwd()}')

padrao_nome = input('Qual o padrão de nomes de arquivos a usar (sem a extensao)?')

#separando os ar4quivos e atributir contador e nome de arquivo
for contador, arquivo in enumerate(os.listdir()):
    #verificar se é um arquivo
    if os.path.isfile(arquivo):
        nome_arq, extern_arq =  os.path.splitext(arquivo)
        nome_arq = padrao_nome + ' ' + str(contador)
        
        nome_novo = f'{nome_arq}{extern_arq}'
        os.rename(arquivo, nome_novo)
        
print(f'\nArquivos renomeados.')