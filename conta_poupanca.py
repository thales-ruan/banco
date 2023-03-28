from conta import Conta
from rendimento_poupanca import RendimentoPoupanca


class ContaPoupanca(Conta):
    def __init__(self, id_conta, saldo,extrato):
        super().__init__(id_conta, saldo,extrato)
        self._rendimento = RendimentoPoupanca(6.0)

    @property
    def rendimento(self):
        return self._rendimento

    @rendimento.setter
    def rendimento(self, novo_rendimento):
        self._limite = novo_rendimento

    def mostrar_extrato(self):
        self._extrato.mostrar_extrato()

    def depositar(self, valor):
        print(f"Depositado R$ {valor:.2f} na Conta Poupança")
        self._extrato.adicionar_transacao("Depósito", valor)
        self._saldo += valor
        print(f"Saldo após depósito: R$ {self._saldo:.2f}")

    def sacar(self, valor):
        
        try:
            if valor > self._saldo:
                raise ValueError("Saldo insuficiente para realizar o saque")
            self._saldo -= valor
            print(f"Saque realizado R$ {valor:.2f} da Conta Poupança")
            print(f"Saldo após saque: R$ {self._saldo:.2f}")
            self._extrato.adicionar_transacao("Saque", valor)
        except ValueError as e:
            print(e)


    def rendimentos(self):
        self._rendimento.calcular_rendimentos(self)


