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


[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 1500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 10
repeticao = 0

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = int(input("valor de deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito:R$ {valor:.2f}\n"
            print(extrato)
        if valor <=0:
            repeticao += 1
            if repeticao == 3:
                print("numero de tentaivas ultrapassou 3 conta bloqueada")
                break
        else:
            print("operacção invalida")

    elif opcao == "2":
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
            saldo_anterior = saldo
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            print(extrato)
            saldo_retirado = saldo_anterior - saldo
            print(f'saldo atual {saldo_anterior} - {saldo_retirado} = {saldo}')
            numero_saques += 1
        
        else:
            print("operação falhou")
        
    elif opcao == "3":
        print("\n================EXTRATO=============")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=======================================")
            
        
    elif opcao == "4":
        break