'''
Aqui, vamos desenvolver alguns exercícios próprios.

1) Crie um algoritimo de lista de compra. As funcionalidades são:

a) Coletar nome do usuário.
b) Coletar um item por vez.
c) fazer alterações de itens.
adicionar itens ao final.
d) retirar itens
e) visualiar itens

não necessariamente nessa ordem.

Vamos usar todo o conhecimento dos métodos de string, contidos no arquivo string_methods.py em alguma pasta por aqui...
'''

compras = []

name = input('Qual o seu nome? \n')

con1 = input(f'Olá, {name.capitalize()}. Gostaria de montar sua lista de compras? [SIM] OU [NÃO] e enter:\n')

if con1.lower() == 'sim': #estamos garantindo que a máquina receberá um sim, seja o user escrevendo SIM ou Sim ou qualquer modo.
    while True: # enquanto con1.lower() == 'sim'
        # menu de opções
        print('Escolha uma opção:')
        print('1. Adicionar itens')
        print('2. Alterar item')
        print('3. Remover item')
        print('4. Exibir lista')
        print('5. Sair')
        
        op = input('Digite o número da opção desejada e pressione enter: \n')

        if op == '1':
            itens = input('Digite os itens que você gostaria de adicionar a lista separados por virgula e ao final, pressione enter para confirmar: \n')

            lista_itens = [item.strip() for item in itens.split(',')]
            compras.extend(lista_itens)
            print('Itens adicionados!\n')
        
        elif op =='2':
           print('Sua lista de compras possui os seguintes itens:')
           '''
           Aqui, devemos enumerar a lista se formos mostrá-la sem ser no formato de lista tradicional ['item1', 'item2',..., 'itemn'].

           Isso porque, para o user, mostrar a lista em cascata é mais amigável:

           1. Item1
           2. Item2
           3. Item3
           .
           .
           .
           n. Item'n'

           Para fazer um print no visual acima, sem os números ao lado e sem índice, podemos simplesmente usar o comprehension list [print(f'{i}') for i in compras]. Mas, como escolheríamos o item que queremos alterar? precisaríamos fazer uma referÊncia a lista de modo mais literal. Nossa intenção é simplificar o processo. Nesse sentido, utilizaremos o método enumerate() para atribuirmos indices aos itens da lista, e podermos alterar o produto escolhido.
           '''
           [print(f'{i+1}. {item}') for i,item in enumerate(compras)] #mostra os itens da lista

           ialt = int(input('Digite o número do item que você deseja alterar e pressione enter: \n'))
           new_item = input(f'\nDigite o item que você deseja colocar no lugar do {compras[ialt - 1]}:\n')
           compras[ialt-1] = new_item
           print('\nSua lista atualizada:\n')
           [print(f'{j+1}. {item}') for j,item in enumerate(compras)]
        
        elif op == '3':
            if len(compras) == 0:
                print('Sua lista está vazia.')
            else:
                print(f'Esta é sua lista até o momento:\n')
                [print(f'{k+1}. {item}') for k,item in enumerate(compras)]
                iex = int(input('\nDigite o número do item que deseja excluir: \n'))
                if iex-1 <0 or iex-1 > len(compras):
                    print('Número inválido! \n')
                else:
                    compras.pop(iex-1)
                    print('Esta é sua lista atualizada:')
                    [print(f'{k+1}. {item}') for k,item in enumerate(compras)]

        elif op =='4':
            if len(compras) == 0:
                print('Sua lista está vazia!')
            else:
                print('\n Esta é a sua lista atual: \n ')
                [print(f'{k+1} {item} \n') for k, item in enumerate(compras)]
        
        elif op == '5':
            print(f'Até mais, {name.capitalize()}.')
            break
else:
    print('BLZ! Os de verdade eu sei quem são.')

'''
Bem, até aqui, tudo funcionando. Glória a Deus.

'''