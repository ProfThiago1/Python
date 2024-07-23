'''
Uma função que chama a si mesma. Não tem muito o que falar, só meter a mão na massa.

Minto, o conceito é razoavelmente o mesmo de recursividade da matemática.

'''

'''def rec(k):
    if (k>0):
        result = k + rec(k-1)
        print(result)
    else:
        result=0
    return result

print('Resultados:')
rec(4)
'''
def fact(n):
    if (n>0):
        res = n*fact(n-1)
    else:
        res=1
    return res

m = 3
resultado = fact(m)

print(f'{m}! = {resultado}')
