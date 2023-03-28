from conta_corrente import ContaCorrete
from conta_poupanca import ContaPoupanca
from extrato_bancario import ExtratoBancario

#Dica pra executar: Comente todas as linhas e vai executando uma por vez para ver cada coisa de uma vez

#EXEMPLO DE UTILIZAÇÃO DO PROGRAMA
#Se cria as conta assim, passando Essas propiedades
conta_corrente = ContaCorrete (id_conta=1, saldo= 600,limite= 200,extrato=ExtratoBancario())
conta_poupanca = ContaPoupanca(id_conta=2, saldo= 4000,extrato=ExtratoBancario())


###Exemplo Utilização Conta Corrente
print("\nConta Corrente:")
print(f"Saldo inicial: R$ {conta_corrente.saldo}")
print(f"Seu Limite de cheque Especial é: R$ {conta_corrente.limite}")

conta_corrente.depositar(100) #Deposita 100R$ Na conta corrente |valor final (Saldo:700) (Limite:200)
conta_corrente.sacar(150) #Saca 150R$ na conta corrente |valor final(Saldo:550) (Limite:200)
conta_corrente.sacar(650) #Sacando Acima do meu saldo, assim descontando uma quantia do meu limite (Saldo:0) (Limite:100)
conta_corrente.sacar(300) #Saque negado sem saldo e limite suficiente
conta_corrente.depositar(200) #Deposito, Paga primeiro o valor do limite e o resto vai para o saldo (Saldo:100) (Limite:200)
conta_corrente.mostrar_extrato() #Com essa Função vai exibir em ordem todas trancaçoes feita acima assim facilitando o entendimento

print("**********************") #Apenas separa as contas na exibição

###Exemplo Utilização Conta Poupança
print("\nConta Poupança:")
print(f"Saldo inicial: R$ {conta_poupanca.saldo}")
conta_poupanca.depositar(500) #Deposita R$500 na conta poupança |valor final (Saldo:4500)
conta_poupanca.sacar(1000)#Saca R$1000 conta poupança |valor final (Saldo:3500)
conta_poupanca.sacar(5000) #Saque negado sem saldo suficiente
conta_poupanca.mostrar_extrato()# Mostra as trançacoes acima
conta_poupanca.rendimentos() # Essa é uma função dinamica vai pedir o tempo que voce quer consultar voce digita o numero correspondente e depois o tempo (sobre o saldo)









