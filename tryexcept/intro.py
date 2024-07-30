
'''
Sempre que algo de errado acontece, o python nos retorna uma mensagem de erro. Podemos personalizar mensagens de erro com os blocos try e except.
Sempre que o bloco try retornar um erro, o bloco except será executado.

'''

try:
    print(y)
except:
    print('A variável x não está definida no escopo.')