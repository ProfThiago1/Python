#Aqui, criaremos uma estrutura de dados composta (lista) e realizaremos #as operações usuais de um banco de dados estruturado:

#Adicionar itens; [ok]
#Excluir itens; [ok]
#Pesquisa se um item está no banco de dados; [ok]
#Classificar o tipo de dado. [ok]

list =[]

numbers =[10,9,8,7,6,5,4,3,2,1]
for n in numbers:
   list.append(n)
list.remove(1)
if 9 in list:
   print('O 9 está na lista')
print(list)
print(type(list[0]))