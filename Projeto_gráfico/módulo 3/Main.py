class Pessoa:
    "Isto é uma classe nova chamada Pessoa"
    idade = 15
    def saud(self):
        print('olá Pessoas!')

#criando um novo objeto para a classe Pessoa

Matheus = Pessoa()

print(Matheus.idade)
print(Matheus.saud)
print(Matheus.__doc__)

Matheus.saud() #não precisou de um print, pois o prórpio método saud() já possui um print interno.

# Se chamarmos o método saud() dentro de um print, a mensagem será exibida duas vezes:

print(Matheus.saud()) #[ok]