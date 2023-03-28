from datetime import datetime
from interface_extrato import Extrato


class ExtratoBancario(Extrato):        
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, tipo, valor):
        transacao = {
            "data": datetime.now(),
            "tipo": tipo,
            "valor": valor
        }
        self._transacoes.append(transacao)

    def mostrar_extrato(self):
        print("***Extrato***")
        for transacao in self._transacoes:
            data = transacao["data"].strftime("%d-%m-%Y")
            tipo = transacao["tipo"]
            valor = transacao["valor"]
            print(f"{data} | {tipo} = R$ {valor:.2f}")