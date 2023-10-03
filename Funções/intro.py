# Criar um função para ler duas notas dos alunos [ok]

# Função para calcular a média [ok]

# criar um laço para definir a situação do aluno [ok]

def notas ():
    n = float(input('Digite uma nota para o aluno(a): '))
    return n

def result(n1,n2):
    mean = (n1 + n2)/2
    print(f'Nota 1: {n1}')
    print(f'Nota 2: {n2}')
    print(f'Média: {mean}  Resultado:', end='')
    if mean >= 7:
        print('Aprovado(a)!')
    elif mean>=5 and mean<7:
        print('Recuperação.')
    else:
        print('Reprovado(a).')
    
#Chamando as funções na tela do usuário
a = notas() 
b = notas()

resultado = result(a,b) # onde n1 = a e n2 = b