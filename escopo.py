#Escopo global: é declarada fora de funções e pode ser acessada por todo o código
#Escopo local: é acessada apenas dentro da função

var_global = 'Curso Completo de Python'
def escreve_texto():
    #para alterar uma variável global a partir do escopo de uma função é necessário usar
    #a palavra chave global, ex.:
    global var_global
    var_global = 'banco de dados sql'
    #obs: a nova atribuição para a variável global deve ser feita separada da linha onde é descrito a
    #palavra chave global
    var_local = 'variável local'
    print(f'Variável global: {var_global}')
    print(f'Variável local: {var_local}')
    
if __name__ == '__main__':
    print(f'Executar a função escreve_texto()')
    escreve_texto()
    
    print('tentar acessar as variáveis diretamente')
    print(f'Variável global: {var_global}')
