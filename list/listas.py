'''
São objetos indexados, ordenados e podemos realizar buscas, acessos, add, remove etc.

Pode guardar diversos tipos de dados: ['maçã', 2, True]
'''

l1 = ['Café', 'arroz', '2 kg de frango', 'macarrão', 'bata doce']

# print certas partes da lista

print(l1[:4])

#verificar existência de itens na lista

if "macarrão" in l1:
    print("Tem macarrão na lista.")
else:
    print("vocÊ esqueceu o macarrão")