#Orientação a Objetos
#pyhton é multiparadígmas
#Classes e Objetos

#criando uma classe (sempre com letra maiúscula)

class Veiculo:
    
    #métodos:
    #self: para dizer que se refere ao proprio objeto
    #método construtor(INIT em python):
    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante # com o underscore antes do atributo ele se torna privado
        #self.fabricante = fabricante #sem o underscore antes do atributo o torna pulico
        self.__modelo = modelo
        self.__num_registro = None
    
    #Método getter para acessar os atributos
    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}')
    
    #método Setter para gravar dados nos atributos
    def set_num_registro(self, registro):
        self.__num_registro = registro
        
    def get_num_registro(self):
        return self.__num_registro
            
    
    def movimentar(self):
        print(f'Sou um veículo e me desloco.')

#herança
#colocar a classe mãe dentro dos parenteses
class Carro(Veiculo):
    #método __init__ será herdado
    
    def movimentar(self):
        print(f'Sou um carro e ando pelas ruas.')   
        
class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__categoria = categoria
        super().__init__(fabricante, modelo)   #indica q todo o resto é igual à classe mãe        
        
if __name__ == '__main__':
    meu_veiculo = Veiculo('gm', 'cadillac escalade')
    meu_veiculo.movimentar() 
    meu_veiculo.get_fabr_modelo()   
    meu_veiculo.set_num_registro(4654656)
    print(f'Registro: {meu_veiculo.get_num_registro()}') 
    
    meu_carro = Carro('volkswagem', 'polo')
    meu_carro.movimentar()
    meu_carro.get_fabr_modelo()
       

           