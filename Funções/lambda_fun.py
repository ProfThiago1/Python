'''
Funções lambda são "funções de uma linha" com n argumentos, mas somente uma expressão (ação).

Sintaxe
-------

lambda args: expressão

Ex: x = lambda n : n + 1

print(x(2)) ---> 3

'''

lambda_func = lambda n,m: (n+1-m)*(-1)
print(lambda_func(2,4))