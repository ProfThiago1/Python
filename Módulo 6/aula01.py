# Nesta aula, iremos aprender sobre a manipulação de arquivos de texto (.txt)

# O primeiro comândo é a função open(), que a sintaxe: arquivo = open ('nopme do arquivo.txt', 'w'). 'write' == escrever no arquivo.

#arquivo = open('arquivo.txt', 'w', encoding='utf-8')

#arquivo.write('Testando o método write de escrita \n')
#arquivo.write('Aula prática')
#arquivo.close()

#with open('arquivo.txt', 'r', encoding='utf-8') as leitura: #uma forma diferente de chamar a função open e a função read.
 #   print(leitura.read())
#leitura.close()

#-----------------------------------------#
#Outros métodos de leitura e escritas de arquivos


with open('arquivo.txt','a+', encoding='utf-8') as arquivo:
    arquivo.write('\n Escrevendo na última linha.')
    arquivo.close()

with open('arquivo.txt', 'r', encoding='utf-8') as leitura:
    print(leitura.read())
