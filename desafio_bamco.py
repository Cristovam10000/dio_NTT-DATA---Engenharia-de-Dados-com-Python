# def deposito(valor, saldo):
#     saldo += valor
#     return saldo

# saldo = 0
# while True:
#     valor = int(input("digite um valor ou [0] se desejar sair: "))
#     if valor == 0:
#         opcao = input("gostaria de receber o extrato: ")
#         if opcao.lower() == "sim":
#             print(f"seu saldo atual é de {saldo}")
#         else:
#             print("volte sempre")        
#         break
#     saldo = deposito(valor, saldo)
  
menu = """


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = int(input("valor de deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito:R$ {valor:.2f}\n"
        else:
            print("operacção invalida")

    elif opcao == "s":
        valor = float(input("indique o valor desejado para saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite  
        excedeu_saque = numero_saques >= LIMITE_SAQUES 

        if  excedeu_saldo:
            print("vc não tem saldo suficiente")
        elif excedeu_limite:
            print("vc utrapassou o limite de saque de R$ 500")
        elif excedeu_saque:
            print("vc utrapassou o limite de saques ou seja tentou savcar mais de 3 vezes")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("operação falhou")
        
    elif opcao == "e":
        print("\n================EXTRATO=============")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=======================================")
            
        
    elif opcao == "q":
        break