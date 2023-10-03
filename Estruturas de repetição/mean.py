# Para melhor compreensão sobre a estrutura de repetição While, vamos criar uma classe chamada MediaValores, na qual o usuário digita vários valores reais positivos.
# Todos estes números devem ser somados e, quando for digitado algum número negativo, o laço de repetição deverá encerrar e, na sequência, exibir a média dos valores digitados.

N = 0 #número total de elementos ou números
soma = 0
mean = 0
valor = valor = float(input('Digite um número:'))

#laço while():
while (valor > 0.0):
    N+= 1
    soma+=valor
    valor = float(input('Digite um número:'))
#  Se o número digiado for negativo, break:
mean = soma/N

print(f'A soma dos {N} valores é igual a {soma}. Além disso, a média é {mean:.2f}')