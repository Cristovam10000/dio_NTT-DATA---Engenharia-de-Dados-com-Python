frutas = ['laranja',"maça","uva","pera"]
print(frutas[0])
print(frutas[2])
print(frutas[-1]) #sempre ultimo termo

letras = list("python")
print(letras)

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]
print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

lista = ["p","y","t","h","o","n"]

print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])
# ///////////////////////////////////////////////////////////////////////
carros  = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros, start=1):
    print(f'{indice}: {carro}')

# ///////////////////////////////////////////////////////////////////////
numeros = [1,30,21,2,9,65,34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)
# for numero in numeros:
#     if numero % 2 == 0:
#         pares.append(numero)
# print(pares)
# ///////////////////////////////////////////////////////////////////////

numeros1 = [1,30,21,2,9,65,34]
quadrado = [numero**2 for numero in numeros1]
print(quadrado)

