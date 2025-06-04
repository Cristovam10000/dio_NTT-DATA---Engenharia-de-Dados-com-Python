frutas  = ("laaranja", "pera", "uva",)

frutas[0]
frutas[-1]

# conjuntos
# set elimina duplicatas

set([1,2,3,4,3,4,3,5])
set("abacaxi")
set(("palio", "gol", "laranja", "palio"))

linguagens = {"python", "java", "python"}
print(linguagens)

conjunto_a = {1, 2}
conjunto_b = {2, 4}

print(conjunto_a.union(conjunto_b))

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.intersection(conjunto_b))
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))
print(conjunto_a.symmetric_difference(conjunto_b))
print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

conjunto_c = {1,2,3,4,5}
conjunto_d = {6,7,8,9}
conjunto_e = {1,0}

print(conjunto_c.isdisjoint(conjunto_d))
print(conjunto_c.isdisjoint(conjunto_e))

sorteio = {1,2}

print(sorteio.add(25))
print(sorteio.clear())
print(sorteio.copy())
print(sorteio.discard(1))
print(sorteio.pop())
print(sorteio.remove(2)) #se dircarta um numero que mão exiti no conjunto ele vai dar erro difrente de usar o discard 
