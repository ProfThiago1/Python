class Main:
    pass

#print('testando o projeto')

from Cliente import Cliente
from Conta import Conta

c1 = Cliente('João','84 9 99124895')

conta = Conta(c1.nome__,2145,0)


print(f'Olá, {c1.nome__}. Seu número de telefone é {c1.telefone}.\n Na sua conta {conta.numero}, seu saldo é R$ {conta.saldo}.')

