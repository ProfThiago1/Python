"""
Aqui revisaremos os conceitos de escrita, leitura, atualização e exclusão de arquivos com o método ope() e suas chaves.

"""

f = open("demo.txt", 'r', encoding='utf-8')
print(f.read())
f.close()