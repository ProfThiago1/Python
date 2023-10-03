# Treinando condições

lista = [234,654,378,798, 955]

for i in lista:
    #Se o resto da divisão por 3 for 0:
    if i%3 ==0:
        #print
        print(f'{i}/3 = {i/3}')
    elif i%3 !=0:
        print(f'O número {i} não é divisível por 3')