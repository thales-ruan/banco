from conta import Conta

class ContaCorrete(Conta):
    def __init__(self, id_conta, saldo, extrato, limite):
        super().__init__(id_conta, saldo,extrato)
        self._limite = limite
        self._limite_devido = 0

    @property
    def limite(self):
        return self._limite
    
    @limite.setter
    def limite(self, set_limite):
        self._limite = set_limite

    @property
    def limite_devido(self):
        return self._limite_devido
    
    @limite_devido.setter
    def limite_devido(self, set_limite_devido):
        self._limite_devido = set_limite_devido

    def mostrar_extrato(self):
        self._extrato.mostrar_extrato()    

    def saldo_disponivel(self):
        return self._saldo + self._limite
    
    def depositar(self, valor):
        print(f"Depositado R$ {valor:.2f} na Conta Corrente")
        self._extrato.adicionar_transacao("Depósito", valor)

        if self._limite_devido > 0:
            valor_pago = min(self._limite_devido, valor)
            self._limite_devido -= valor_pago
            valor -= valor_pago
            self._limite += valor_pago
            print(f"Pagando R$ {valor_pago:.2f} do valor devido no cheque especial")
            self._extrato.adicionar_transacao("Valor pago Cheque-especial", valor_pago)
        self._saldo += valor
        print(f"Saldo após depósito: R$ {self._saldo:.2f}")

    def sacar(self, valor):
        try:
            if valor > self.saldo_disponivel():
                raise ValueError("Saldo e limite insuficientes para realizar o saque")
            else:
                if valor <= self._saldo:
                    print(f"Saque realizado R$ {valor:.2f} da Conta Corrente")
                    self._extrato.adicionar_transacao("Saque", valor)
                    self._saldo -= valor
                else:
                    saque_limite = valor - self._saldo
                    self._saldo = 0
                    if saque_limite <= self._limite:
                        self._limite -= saque_limite
                        self._limite_devido += saque_limite
                        self._extrato.adicionar_transacao("Saque no valor", valor)
                        self._extrato.adicionar_transacao(f"Seu saque de = R$ {valor:.2f} usou o limite do Cheque-especial em", saque_limite)
                    else:
                        raise ValueError("Saldo e limite insuficientes para realizar o saque")
        except ValueError as e:
            print(e)
        finally:
            print(f"Saldo após saque: R$ {self._saldo:.2f}")


            