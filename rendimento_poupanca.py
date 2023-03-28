from interface_rendimento import Rendimento

class RendimentoPoupanca(Rendimento):
    def __init__(self, taxa_rendimento):
        self._taxa_rendimento = taxa_rendimento

    def calcular_rendimentos(self, conta):
        opcoes_tempo = {
            1: "ANOS",
            2: "MESES",
            3: "SEMANAS",
            4: "DIAS",
            5: "HORAS",
            6: "MINUTOS",
            7: "SEGUNDOS"
        }

        print("Olá, como deseja ver o seu rendimento?")
        for opcao, descricao in opcoes_tempo.items():
            print(f"{opcao}: {descricao}")

        while True:
            try:
                opcao_escolhida = int(input("Digite o número da opção escolhida: "))
                if opcao_escolhida in opcoes_tempo:
                    break
                else:
                    print("Valor inválido, tente novamente.")
            except ValueError:
                print("Valor inválido, tente novamente.")

        unidade_tempo = opcoes_tempo[opcao_escolhida]

        while True:
            try:
                quantidade_tempo = float(input("Por quanto tempo deseja calcular? (Digite apenas números): "))
                if quantidade_tempo > 0:
                    break
                else:
                    print("Valor inválido, por favor digite um valor maior que 0.")
            except ValueError:
                print("Valor inválido, por favor digite apenas números.")

        rendimento_por_tempo = {
            "SEGUNDOS": 3153600000,
            "MINUTOS": 52560000,
            "HORAS": 876000,
            "DIAS": 36500,
            "SEMANAS": 5200,
            "MESES": 1200,
            "ANOS": 100,
        }

        unidade_tempo = unidade_tempo.upper()
        if unidade_tempo not in rendimento_por_tempo:
            raise ValueError("Unidade de Tempo Inválida.")

        rendimento = (self._taxa_rendimento * quantidade_tempo * conta.saldo) / \
            rendimento_por_tempo[unidade_tempo]
        print(
            f"O seu saldo de R$ {conta.saldo:.2f} renderá R$ {rendimento:.2f} em {quantidade_tempo} {unidade_tempo.lower()} tendo como base o juros da poupança que é de {self._taxa_rendimento} ao ano.")
