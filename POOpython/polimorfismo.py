'''
O polimorfismo é literalmente 'muitas formas'. Aqui, o polimorfismo se refere aos métodos, funções e operações de mesmo nome que podem ser executadas em muitos objetos ou classes.

O intuito desse bloco é revisar a sintaxe e afins.
'''

'''# Diferentes classes com mesmo nome de método

class Car:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
    # Método mover-se:
    def move(self):
        print('Dirigindo...')

class Barco:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
    # método mover-se
    def move(self):
        print('Navegando...')

class Aviao:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
    # método mover-se
    def move(self):
        print('Voando...')

c = Car('Toyota', 'Corola')
b = Barco('bgt', 'bgt1000')
a = Aviao('Gol', 'Airprime')

for i in (c,b,a):
    i.move()
    
O exemplo anterior pode ser "melhorado" utilizando o conceito de herança. Note que, podemos colocar o carro, o barco e, o avião, todos como classes filhas/subclasses de uma classe chamada veículos. é o que faremos abaixo.    

'''

# Exemplo utilizando o conceito de herança
# A classe pai é a Veiculo

class Veiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
    def move(self):
        print('Dirigindo...')


class Carro(Veiculo):
    pass

class Barco(Veiculo):
    pass
    def move(self):
        print('Navegando...')
        '''
        Na classe Barco, não utilizamos o método super() na função move porquê a aplicação dele será diferente da forma que é aplicada pela classe pai e a subclasse Carro.

        Não precisamos do construtor __init__() porquê não vamos construir outro atributo para a classe Barco.
        '''

class Aviao(Veiculo):
    pass
    def move(self):
        print('Voando..')

# Instanciando os objetos

c = Carro('Pegeout', '206')
b = Barco('Barco top', 'de luxo')
a = Aviao('Boing', '756')

for y in (a,b,c,):
    print(y.modelo, y.marca)
    y.move()