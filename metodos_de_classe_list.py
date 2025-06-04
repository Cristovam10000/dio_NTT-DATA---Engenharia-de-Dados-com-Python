lista = []

lista.append(10)
lista.append([20,30,4,5,])
print(lista)

lista.clear()
print(lista)

# ///////////////////////////////////////////////////////////////////////

lista = [1, "python", [40,20,9,19]]

l2 =lista.copy()

print(lista)
print(id(l2), id(lista))

# ///////////////////////////////////////////////////////////////////////

cores = ["vermelho","vermelho","azul","verde","azul"]

print(cores.count("vermelho"))
print(cores.count("azul"))

# ///////////////////////////////////////////////////////////////////////

linguagens = ["python", "js","c"]

print(linguagens)

linguagens.extend(["java", "csharp"])

print(linguagens)

# ///////////////////////////////////////////////////////////////////////

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))
print(linguagens.index("python"))

# ///////////////////////////////////////////////////////////////////////

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop(0))

# ///////////////////////////////////////////////////////////////////////

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")
print(linguagens)

linguagens.reverse()
print(linguagens)

# ordena em ordem alfabetica
linguagens.sort()
linguagens.sort(reverse=True)
# por tamnho das palavras do menor para o menor
linguagens.sort(key=lambda x: len(x))
print(linguagens)
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)

