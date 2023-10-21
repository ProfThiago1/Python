# Pedir para o usuário colocar 3 canais e aumentar o volume da tv:

from funcionalidades import *

# Criando o objeto tv da classe Televisor:
tv = Televisor('LG', 'K84')
# Criando um controle remoto na classe ControleRemoto para controlar a tv:
control = ControleRemoto(tv)

# criando o input para o user digitar o nome do canal

ch1 = input("Qual canal você gostaria de adicionar: \n")
control.sintcanal(ch1)
control.trocadecanal(ch1)

#Mostrando na tela o canal e a lista de canais:

print(f'O canal atual é {tv.canal_atual}, e alista de canais até o momento é {tv.list_canal}')

ch2 = input("Qual canal você gostaria de adicionar: \n")
control.sintcanal(ch2)
control.trocadecanal(ch2)
print(f'O canal atual é {tv.canal_atual}, e alista de canais até o momento é {tv.list_canal}')

ch3 = input("Qual canal você gostaria de adicionar: \n")
control.sintcanal(ch3)
control.trocadecanal(ch3)
print(f'O canal atual é {tv.canal_atual}, e alista de canais até o momento é {tv.list_canal}')