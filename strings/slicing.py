'''
Aqui, aprenderemos a "cortar" partes de strings e retorná-las em tela, por meio do índice ocupado na string completa.
'''

h = 'Hello, World!' #Repare que, na contagem do python, temos 12 "espaços" na string, começando do 0"

#retornando parte da string:

print(h[2:5]) #espera-se que o terminal mostre llo. [ok]

'''
A representação do intervalo [2:5] é um intervalo que começa em 2 mas não inclui o 5. Matematicamente, [2,5).

Em geral, vamos tomar o intervalo como sendo dado por dois números inteiros n e m tal que [n:m] representa o intervalo de fatiamento pretendido e, [n:m-1] representa o intervalo real.
'''

#Slice from the start

'''
Slice from the start consiste em iniciar o fatiamento da string do início até um certo ponto (m-1 pontos) da string. Na notação dos colchetes: [:m], onde n é a posição pretendida.
'''

print(h[:5]) #espera-se Hello, ou seja, de 0 até m-1 [ok].

# Slice to the end

''' Slice to the end é o oposto do slice from the start, isto é, agora pegamos um início genérico, por exemplo 2, e vamos até o final da string. Em notação dos colchetes: [1:]'''

print(h[1:]) #espera-se ello, World [ok].

#Negative indexing


'''
A ideia aqui é usar indices negativos para cortar a string a partir de o fim dela. Nesse sentido, em 'Hello, World!' a posição -2 corresponde a letra d; a posição -5 corresponde a letra o, e assim sucessivamente.
'''

print(h[-5:-1]) # [-5,-1) vamos de o até d [ok]