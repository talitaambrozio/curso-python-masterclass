#Exceções forçadas

from math import sqrt

if __name__ == '__main__':
    try:
        num = int(input('Digite um número positivo: '))
        if num < 0:
            raise ArithmeticError
    except ArithmeticError:
        print(f'Foi fornecido um número negativo!')
    else:
        print(f'A raiz quadrada de {num} é {sqrt(num)}')
    finally:
        print(f'Fim do cálculo.')           