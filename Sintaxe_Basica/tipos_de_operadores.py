# comparção
x = 200
y = 450
print(x == y)
print(x >= y)
print(x <= y)
print(x != y)
print(x > y)
print(x < y)

# atribuição(utilizados para definir o valor inicial ou sobrescrever o valor de uma variavel)
saldo = 500
saldo +=200 
print(saldo)
saldo -= 100
print(saldo)
saldo *= 2
print(saldo)
saldo /= 5
print(saldo)
saldo //= 5
print(saldo)
saldo **= 34
print(saldo)
saldo %= 15
print(saldo)

# curiosidades
resultado = 10 / 3
print(f"{resultado:.2f}")

# operadores logicos(utilizados junto com o de comparação, para montar uma expressão logica)
saldo = 1000
saque = 200
limite = 100
conta_especial = True
contatos_emergencia = []
print(saldo >= saque and saque <= limite)
print(saldo >= saque or saque <= limite)
print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))
# negação da afirmação
print(not 1000 > 1500)
print(not contatos_emergencia)
print(not "saque 1500;")

# operadores de identidade(se dois objetos testados ocupam a mesma posição na memoria)
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

print(curso is nome_curso)
print(curso is not nome_curso)
print(saldo is limite)

# operadores de associação(verificar se um objeto está presente em uma sequência)
frutas = ["limão", "uva"]
print("laranja" in frutas)
