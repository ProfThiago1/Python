#Reproduzir a ideia do ex003 com laços

from funcionalidades import *

tv = Televisor('LG', 'K84')

control = ControleRemoto(tv)

i=0
while i <=3:
    ch = input('Digite o nome do canal que você deseja sintonizar: \n')
    control.sintcanal(ch)
    control.trocadecanal(ch)
    i+=1
print(f' Esses são os canais sintonizados: {tv.list_canal}')

v = input('O volume atual está em 20. Gostaria de aumentar? Digite S para sim, ou N para não. \n')

if v == 'S' or v == 's':
    v_plus = int(input('Digite o valor que você quer aumentar: \n'))
    control.aumentarvol(v_plus)
    vs = tv.volume
    print(f'O novo volume é {vs}')