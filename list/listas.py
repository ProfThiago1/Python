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

# mudar itens da lista

l1[4] = 'macaxeira'
#print(l1)


#adicionando em certa posição, sem retirar is itens anteriores

l1.insert(2, "cuscuz")

print(l1)

# adicionar ao fim append()

l1.append('biscoito')

print(f'sua lista de compras é {l1}')

# adicionar elementos de uma outra lista extend()

l2 = ['creme dental', 'fio dental', 'sabão', 'amaciante']

l1.extend(l2)

print(f"Sua lista de compras: {l1}")

# remover itens:
'''
Podemos usar alguns métodos para remover itens de uma lista:

I) remove()

lista.remove('item') remoção usando o 'remove()' remove o item entre parÊnteses.

se houver mais de uma ocorrência do 'item', o método remove()  remove a primeira ocorrÊncia.

l1 = ['a', 'b','a']

l1.remove('a')

print(l1) ---> ['b','a']

II) pop()

o método pop(index) remove um item da lista identificado pelo seu índice. Por exemplo:

l1.pop(1)
print(l1) ---> ['a','a']




III) del

a palava chave 'del' remove um item com índice específico assim como faz o método pop():

del l1[0]

print(l1) --- > ['b','a']



IV) clear()

o método clear() literalmente limpa a lista.


'''

#loops com listas


# I) loop para mostrar os elementos da lista

fruits = ['banana', 'apple', 'cherry', 'watermelon'] 

for f in fruits:
    print(f)

# II) loop na lista por um intervalo que se encaixe no comprimento da lista


for f in range(len(fruits)-1):
    print(fruits[f]) 

    ''' Aqui, notemos que len(fruits)==3, ou seja, meu renge == [0,3]. Então, qunado escrevo range(len(fruits) - 1), estou dizendo que meu loop deve ir de 0 à 2, isto é, só deve ser mostrados os itens com os índices de 0 à 2.'''
print(len(fruits)) # comprimento igual a 4.



# while

f = 0
while f < len(fruits):
    print(fruits[f])
    f+=1 


# Compressão de listas

'''
"List Comprehension" é um 'shorter syntax' para criarmos uma lista baseada em items de uma lista já existente, sob condições específicas.

Por exemplo, na lista fruits = ['banana', 'apple', 'cherry', 'watermelon']

se quisermos uma nova lista de frutas que contenham a letra 'e' no seu nome a partir da lista fruits, o que podemos fazer?

1) Usando a regra do for:
fruits_e = []
for x in fruits:
    if 'e' in x:
        fruits_e.append(x)

2) Usando comprehension

fruits_e = [x for x in fruits if 'e' in x]

em apenas uma linha temos o mesmo resultado.

Vamos analisar a sintaxe:

newlist = [expressão for item in iterable if condition == True]

vamos a um exemplo com números:

n1 = [1,2,3,4,5,6,7,8,9,10]

n2 = [n for n in n1 if n%2==0]

print(n2) --> [2,4,6,8,10]

lemos: n2 recebe n para n em n1 se o resto da divisão de n por 2 for igual a 0, isto é, se n for par, ele deve ser incluido na lista n2.

usando uma expressão de fato:

n3 = [x**2 for x in n2]

print(n3) --> [4,16,36,64,100]


'''