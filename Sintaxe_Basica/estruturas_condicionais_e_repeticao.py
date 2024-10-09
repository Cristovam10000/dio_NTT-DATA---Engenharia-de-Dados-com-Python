def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")



def depositar(valor):
    saldo = 500

    saldo += valor
    print(saldo)

depositar(300)

# ///////////////////////////////////////////////////////////////////////

import sys


saldo = 2000
opcao = int(input("informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1 :
    saque = float(input("informe o valor do saque: "))
    if saldo >= saque:
        print("saque permitido!")
    else:
        print("saque negado!")

elif opcao == 2 :
    print("Exibir o extrato...")
else:
    sys.exit("opção invalida")

# ///////////////////////////////////////////////////////////////////////

# uma outra ideia de codigo que eu tive 
def deposito(valor, saldo):
    saldo += valor
    print(f'o seu saldo agora é {saldo}')
    return saldo

saldo = 0 


while True:
    valor = int(input("gigite um valor ou [0] para depositar: "))
    if valor == 0:
        print("fim da sessão")
        break
    saldo = deposito(valor, saldo)

# ///////////////////////////////////////////////////////////////////////

MAIOR_IDADE = 18

idade =int(input("digite o valor de sua idade: "))

if idade >= 18:
    print("maior de idade pode tirar a CNH")

# ///////////////////////////////////////////////////////////////////////

conta_normal = True
saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("oiiiiiiiii")  

# ///////////////////////////////////////////////////////////////////////

saldo = 2000
saque = 500

resultado = "sucesso" if saldo >= saque else "falha"
print(f'o resultado foi um {resultado}')

# ///////////////////////////////////////////////////////////////////////

valor = int(input("digite a até onde vc quer que o numero chegue: "))

valor += 1 

for x in range(1,valor):
    print(x)

# ////////////////////////////////////////////////////////////////////////

valor = int(input("digite a até onde vc quer que o numero chegue: "))
if valor <=0:
    print("digite um valor positivo")
else:
    numeros = list(range(1,valor + 1))
    print(f'numero de elementos é {len(numeros)}')
    print(numeros)

    for x in numeros:
        print(x)
        

# ///////////////////////////////////////////////////////////////////////

texto = input("informe um texto: ")
vogais = 'AEIOU'

for letra in texto:
    # upper(converte para maiusculo)
    if letra.upper() in vogais:
        print(letra, end="") #esse end="" é para as letras ficarem lado a lado
else:
    print()  # quebra de linha
    print("olá")

# ///////////////////////////////////////////////////////////////////////

for numero in range(1, 11 + 1):
    print(numero, end=" ")
# ///////////////////////////////////////////////////////////////////////

numero = int(input("digite um numero"))
escolha = input("escolha uma opcao")

for x in range(11):
    if escolha == "*":
        resultado = numero * x
    if escolha == "/":
        resultado = numero / x
    if escolha == "+":
        resultado = numero + x
    if escolha == "-":
        resultado = numero - x
    print(resultado)

# ///////////////////////////////////////////////////////////////////////
numero = int(input("digite um numero"))
escolha = input("escolha uma opcao: ")

operacoes = {
    "*": lambda x,y: x * y,
    "/": lambda x,y: x / y if y != 0 else "erro",
    "+": lambda x,y: x + y,
    "-": lambda x,y: x - y
}

for x in range(11):
    resultado = operacoes.get(escolha,lambda x,y: "Operação inválida")(numero, x)
    print(f"{numero} {escolha} {x} = {resultado}")
# ///////////////////////////////////////////////////////////////////////
opcao = 1
while opcao != 0 :
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n :"))
    if opcao == 1:
        print("secando")
    elif opcao == 2:
        print("exibindo extrato")
# ///////////////////////////////////////////////////////////////////////
for numero in range(100):
    if numero % 2 == 0:
        continue
    print(numero, end=" ")
    