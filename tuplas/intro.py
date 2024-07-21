'''
Uma tupla é uma coleção, assim como listas e sets, com propriedades próprias. Tuplas são ordenadas e seus valores são imutáveis.

I) Uso

Utilizamos tuplas para armazenarmos multiplos valores em uma variável:
frutas = ('maçã', 'banana', 'abacaxi')

II) imutabilidade

* não podemos mudar um item de uma tupla no decorrer do código como fazemos em listas. Se tentarmos usar o método usado em listas, receberemos um erro:

frutas[0] = 'coxinha'

print(frutas) --- > TypeError: 'tuple' object does not support item assignment

III) Tipos de dados

Tuplas suportam diversos tipos de dados:

tupla1 = (True, False)
tupla2 = (2,3)
tupla3 = (2, 'string', True)

Podemos usar os métodos de acesso tradicionais via índice do dado na tupla.

* Existe um 'atalho' para mudarmos os itens de uma tupla no decorrer do código. Basta convertermos a tupla em uma lista e, depois de alterarmos o dado, convertermos novamente em uma tupla.

tupla1 = ('a','b')

lista1 = list(tupla1)
lista1[1] = 'mudei'
tupla1 = tuple(lista1)
print(tulpa1) --> ('a', 'mudei') *
 
'''
