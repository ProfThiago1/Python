# Rotinas de repetição while (enquanto)

# print de números [ex. nível 0]
i = 0 #iniciando um contador

#while i<=5:
#    print(f"{i}")
 #   i += 1

# loops irritantes/pegadinhas [ex. nível 0]

#name = "" # Começamos com uma string vazia

#while name != "Seu nome": #Enquanto o "valor" recebido pela var name não for 'Seu nome'
   # print('Digite: Seu nome')
   # name = input()
#print('Você entendeu 🤣.')

# ex. nível 1: Validação de usuário e senha:

while True:
    name = input("Digite seu nome: \n")
    if name != "Thiago":
        print(f'Hum... Não encontrei seu nome na nossa base de dados. \n Verifique se preencheu o seu nome corretamente e tente novamente.')
        continue
    print(f'Olá, {name}. Qual a sua senha? \n')
    pssw = input ()
    if pssw != "bla123":
        continue
    if pssw == "bla123":
        break
print(f"Seja bem-vindo, {name}.")