from abc import abstractmethod
from interface_extrato import Extrato

class Conta:
    def __init__(self,id_conta,saldo,extrato: Extrato) -> None:
        self._id_conta = id_conta
        self._saldo = saldo
        self._extrato = extrato

    @property
    def id_conta(self):
        return self._id_conta
    
    @id_conta.setter
    def id_conta(self, set_id):
        self._id_conta = set_id

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, set_saldo):
        self.saldo = set_saldo

    @property
    def extrato(self):
        return self._extrato

    @extrato.setter
    def extrato(self, extrato: Extrato):
        self._extrato = extrato


    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

