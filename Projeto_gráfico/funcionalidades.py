# A missão aqui é criar uma espécie de biblioteca local para ser utilizada em um outro arquivo.

# criar métodos para aumentar/diminuir volume, trocar e sintonizar um novo canal, adicionando um novo canal à lista (somente se esse canal não estiver nessa lista). No atributo lista de canais, devem estar armazenados todos os canais já sintonizados dessa TV. [ok]

# Criando uma classe chamada televisor com os atributos: Fabricante, Modelo, Canal atual, Lista de canais e Volume.

class Televisor:
    def __init__(self, fab, model): 
        # método construtor para inicializar as variáveis/objetos
        self.fabricante = fab
        self.modelo = model
        self.canal_atual = None # canal atual vazio
        self.list_canal = [] # Ainda não temos canais aqui
        self.volume = 20 # um volume padrão

    #método para aumentar o volume:

    def aumentarvol (self, valor):
        if self.volume + valor <=100:
            self.valor += valor
        else:
            self.volume = 100
    #método para diminuir o volume:

    def diminuirvol (self, valor):
        if self.volume - valor >=0:
            self.volume -= valor
        else:
            print('Valor inválido.')
            self.volume = 0
    #método de trocar de canal (colocar o canal de fato)

    def trocadecanal (self, canal):
        if canal in self.list_canal: 
            # Se o canal digitado estiver na lista de canais, então posso trocar para este canal.
            self.canal_atual = canal
    # método para sintonizar/add novo canal na list

    def sintcanal(self, canal):
        if canal not in self.list_canal:
            self.list_canal.append(canal)
        else:
            print(f'O canal {canal} já está sintonizado. Veja abaixo a lista de canais sintonizados: \n {self.list_canal}')

#Agora criaremos a classe controle remoto:

class ControleRemoto:
    def __init__(self, tv):
        self.tv = tv
    
    # devemos criar métodos para aumentar/diminuir volume, trocar e sintonizar um novo canal, que adiciona um novo canal à lista de canais (somente se esse canal não estiver nessa lista).

    def aumentarvol (self):
        self.tv.aumentavol(90)
    
    def diminuirvol(self):
        self.tv.diminuirvol(90)
  
    def trocadecanal(self,canal):
        self.tv.trocadecanal(canal)
    
    def sintcanal(self, canal):
        self.tv.sintcanal(canal)