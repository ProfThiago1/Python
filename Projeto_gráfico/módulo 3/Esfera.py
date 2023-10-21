# Construir uma classe que tenhanmétodos para calcular área e volume de uma esfera.

# Importando a biblioteca math para acessarmos o valor de pi com math.pi
import math

# Criando a classe:

class Esfera:
    def __init__(self, cor, raio):
        self.cor = cor
        self.raio = raio
  
  #criando os métodos para calcular a área e o volume
    
    def volume(self):
        vol = (4/3)*math.pi*(self.raio)**3
        return vol
    
    def area(self):
        ar = 4*math.pi*(self.raio)**2
        return ar
    
esf01 = Esfera("Vermelha", 4) # Criando o objeto esf01 chamando a classe Esfera()

esf02 = Esfera("Azul", 3)

print(f' O volume da Esfera 1 é {esf01.volume():.2f} cm³')
print(f" O volume da esfera dois é {esf02.volume():.2f} cm³")