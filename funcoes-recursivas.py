#é uma função que chama a si mesma para resolver um problema

#Formula geral para o fatorial
#fatorial(num) = 1, se num = 0 ou se num = 1 (Caso base)
#fatorial(num) = num * fatorial(num -1), para num > 1 (Caso recursivo)
#ex.: 4! = 4 * fatorial(3) = 4 * 3 * fatorial(2) = 4 * 3 * 2 * fatorial(1)
#4! = 4 * 3 * 2 * 1 = 24

def fatorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * fatorial(num - 1)
    
if __name__ == '__main__':
    x = int(input('Digite um número inteiro positivo para calcular seu fatorial: '))   
    try:
        res = fatorial(x)
    except RecursionError:
        print(f'Número fornecido é muito grande ou negativo.')    
    else:
        print(f'Fatorial de {x} é {res}') 
            
        
