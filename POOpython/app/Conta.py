# Criar a class Conta, que será definida recebendo o objeto Cliente, além dos atributos “número” e “saldo”:


class Conta:
    def __init__(self,titular, numero,saldo):
        self._saldo = saldo
        self._titular = titular
        self._numero =numero
