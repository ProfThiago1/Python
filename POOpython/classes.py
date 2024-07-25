'''
Aqui, não discutiremos conceitos de classes e objetos de maneira geral, pois é de conhecimento geral. Vou focar aqui em revisar criação de classes e afins.

O parâmetro self é uma referência a instância da classe atual, e serve para acessar as variáveis que pertencem a classe.

Podemos utilizar outros nomes para substituir o self mas, em geral, as boas práticas nos levam a usar o self.
'''
#Exemplo básico de classe com atributos simples
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    # função de representação legível de um objeto __str__()
    def __str__(self):
        return f'{self.nome}, {self.idade} anos.'
    
    # métodos da classe abaixo
    def falar(self):
        print(f'Olá! Me chamo {self.nome}, tenho {self.idade} anos.')


p1 = Pessoa('Thiago', 25)
#print(p1)
#p1.falar()

# Herança
'''
Aqui, faremos alguns exemplos de como classes filhas herdam métodos e propriedades de classes pai.

A classe Estudante herdará todos os métodos e atributos da classe Pessoa.
'''
 
'''class Estudante(Pessoa): 
    pass
 Se não quisermos adicionar mais métodos a classe Estudande, basta utilizarmos a palavra chave 'pass'. Assim, qualquer objeto instanciado da classe Estudante terá somente os métodos definidos na classe pai, isto é, Pessoa.

É importante notar que, se utilizarmos o método construtor na classe filha, o __init__() da classe filha sobrescreve o construtor da classe pai, ou seja, a classe filha não herda os atributos que foram construidos na classe pai, execeto se utilizarmos explicitamente:

class Filha(ClassePai):
    def __init__(self, nome, idade):
        ClassePai.__init__(self,nome,idade)
.

'''


 # A função super()
'''A função super() permite herdar todos os parâmetros/atributos da classe pai. 
Usamos super__init__(atr1,...,atrn) para inicializar os atributos da super classe (classe pai, neste caso).

O uso do segundo __init__(self,nome,idade, curso) acima de super() me permite definir novos atributos para classe Estudante e, utilizar os atributos da classe pai Pessoa por meio da inicialização feita abaixo com a função super()__init__().
'''

class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso 
   
   # A representação legível do objeto instanciado desta classe, será a mesma que a da classe pai.
    def __str__(self):
        return super().__str__()
    
    def apresentacao(self):
         print(f'Olá! Me chamo {self.nome}, tenho {self.idade} e curso {self.curso}.')

#instanciando novos objetos    
p = Pessoa('Mateus', 22)

e = Estudante('Mateus', 22, 'Engenharia elátrica')

# Chamando os métodos de cada classe.
p.falar()

e.apresentacao()
print(e)