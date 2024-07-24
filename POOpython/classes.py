'''
Aqui, não discutiremos conceitos de classes e objetos de maneira geral, pois é de conhecimento geral. Vou focar aqui em revisar criação de classes e afins.
'''
#Exemplo básico de classe com atributos simples
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    # função de representação legível de um objeto __str__()
    def __str__(self):
        return f'{self.nome}, {self.idade} anos.'


p1 = Pessoa('Thiago', 25)
print(p1)


