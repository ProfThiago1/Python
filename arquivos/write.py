'''
Os métodos de escrita para um arquivo existente são:

I) append 'a' - Acrescenta o conteúdo no fim do arquivo sem sobrescrever o conteúdo exixtente.

II) write 'w' - sobrescreve qualquer conteúdo existente no arquivo.

'''

'''with open('demo2.txt', 'a', encoding='utf-8') as f:
    f.write('\n Este conteúdo é adicionado na última linha do conteúdo existente.')


with open('demo2.txt', 'r', encoding='utf-8') as f:
    print(f.read())


'''

f = open('demo3.txt', 'x', encoding='utf-8')

with open('demo3.txt', 'w', encoding='utf-8') as f:
    f.write('Criei um novo arquivo!')
    
with open('demo3.txt', 'r',encoding='utf-8') as f:
    print(f.read())
    

with open('demo3.txt', 'a', encoding='utf-8') as f:
    f.write('\n Adicionei isso aqui só de zoas.')
    f.close()