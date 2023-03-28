from abc import abstractmethod

class Extrato:

    @abstractmethod
    def adicionar_transacao(self,tipo,valor):
        pass

    @abstractmethod
    def mostrar_extrato(self):
        pass