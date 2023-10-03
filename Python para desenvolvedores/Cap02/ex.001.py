#Calculadora de temperatura

name = input('Qual o seu nome? \n')
T = float(input(f'Qual a temperatura no ambiente, {name}? \n'))
v = input(f'{T} está em C ou em F ? \n')


if v == 'F' or v =='f':
    F_deg = T
    C_deg = (F_deg - 32)*5/9

    print(f'Ok, faremos a conversão para C.')
    print(f'A temperatura em C é {C_deg:.2f} C')
elif v == 'c' or v=='C':
    C_deg = T
    print(f'Bem, então a temperatura é {T:.2f} C.')

again = input('Quer que eu converta para F? Digite S para sim, e N para não.\n')
F_deg = (9/5)*C_deg +32

def f_to_c(F_deg=0):
    if again =='s':
        print(f'{F_deg}')