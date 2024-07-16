'''
Podemos modificar caracteres na string sem ter que voltar onde elas foram definidas.


Podemos colocar em caixa alta partes - ou o todo - de una string. O mesmo vale para colocar em minúsculo.
'''

# Upper Case: Retorna parte ou a string completa em caixa alta.

h = 'hello, world!'

print(h.upper()) # convertemos toda a str em caixa alta.


# Lower Case: Deixar as letras da str minúsculas.
h_1 = h.upper()
print(h_1.lower())


# Remove Whitespace: Literalmente remover espaços em branco do início e do fim de uma string.

ex = ' Isto é um exemplo! '
print(ex) # Com espaços

print(ex.strip()) # sem espaços

'''
Com os dois exemplos acima, podemos perceber a diferença com e sem espaços pelo comando(método/função) stripe()

'''
# Replace String: O método replace() troca uma string por outra

print(ex.replace('!','?')) # Espera-se: Isto é um exemplo? [ok]


#split() separa a string em substrings

print(h.split(",")) # espera-se (de h): ['Hello', 'World!'] [ok]
