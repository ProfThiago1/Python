# criar uma função que receba o nome, número de conta, utilizando as classes Conta e Cliente. [ok]

# O print deve conter o nome, nº da conta, e o saldo (criado por mim)


# Importando as classes criadas: [ok]

from Cliente import Cliente
from Conta import Conta

# criando as funções com os inputs:

def data():
    name = input('Digite seu nome: ')
    conta = int(input('Digite o número de sua conta abaixo, sem letras e sem epaços: \n'))
    foN = int(input('Digite o número de telefone sem espaçamento: \n'))

    return name, conta, foN


# Utilizando as classes criadas:
name, conta, foN = data()
# Quero que a classe Cliente receba como primeiro atributo o conteúdo da variável name, e o segundo, o conteúdo da variável foN
cliente = Cliente(name,foN)
data_cont = Conta(name, conta, 150)

print(f'Olá, {cliente._nome}. Seu número de telefone é {cliente._telefone}. \n Número de conta: {data_cont._numero}. \n Saldo: R$ {data_cont._saldo}.')
