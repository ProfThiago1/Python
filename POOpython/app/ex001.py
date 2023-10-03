# criar uma função que receba o nome, número de conta, e adicione e uma lista de clientes.[ok]

clientes = [] #lista de clientes criada antes das funções [ok];

def data():
    name = input('Digite seu nome:')
    conta = int(input('Digite o número de sua conta sem traço'))
    clientes.append(name)
    clientes.append(conta)
    return name, conta

call = data()
print(f'Olá, {clientes[0]}. Sua conta é a ID: {clientes[1]}.')

