pessoa = {"nome": "Cristovam", "idade":20}
pessoa2 = dict(nome= "Cristovam", idade= 20)

pessoa["telefone"] = "86999806440"

print(pessoa)

# consultar dados
pessoa["nome"]
pessoa["idade"]
pessoa["telefone"]

# sobrescrever
pessoa["nome"] = "Maria"
pessoa["idade"] = 20
pessoa["telefone"] = "86999576"

# estruturas alinhadas: dicionario dentro de outro dicionario
contatos = {
    "cristovam@2020" : {"nome": "Cristovam","telefone": "86999806440"},
    "ray@2020" : {"nome": "Cristovam","telefone": "86999832440"},
    "cris@2020" : {"nome": "Cristovam","telefone": "86999806440", "extra": {"a":1}},
}

print(contatos["cristovam@2020"]["telefone"])
# ou
telefone = contatos["cristovam@2020"]["telefone"]
print(telefone)

extra = contatos["cris@2020"]["extra"]
print(extra)

extra = contatos["cris@2020"]["extra"]["a"]
print(extra)

for chave in contatos:
    print(chave, contatos[chave])

for chave,valor in contatos.items():
    print(chave, valor)

metodos

contatos = {
    "cristovam@2020" : {"nome": "Cristovam","telefone": "86999806440"},
    "ray@2020" : {"nome": "Cristovam","telefone": "86999832440"},
    "cris@2020" : {"nome": "Cristovam","telefone": "86999806440", "extra": {"a":1}},
}
# contatos.clear()
copia = contatos.copy()
copia["cris@2020"] = {"nome": "cris"}

print(contatos["cris@2020"])
print(copia["cris@2020"])

#crias chaves sem vincular nenhum valor
print(dict.fromkeys(["nome","telefone"]))
# valor padrão
dict.fromkeys(["nome","telefone"], "vazio")

# pegar algum valor dentro dodicionario
print(contatos.get("chave"))
print(contatos.get("chave", {}))
print(contatos.get("cris@2020", {}))

# retorna tudo em uma lista de tuplas
print(contatos.items())

# retorna só as chaves 
print(contatos.keys())

# apaga e retorna o valor
print(contatos.pop("cris@2020"))
print(contatos)

# o mesmo que o pop só que vai retirando na sequencia
print(contatos.popitem())

#acrecenta chave e valor se ela tiver já o valor acrecentando não muda nada
contatos2 = {
    "cristovam@2020" : {"nome": "Cristovam","telefone": "86999806440"},
    "say@2020" : {"nome": "Cristovam","telefone": "86999832440"},
    "cris@2020" : {"nome": "Cristovam","telefone": "86999806440", "extra": {"a":1}},
}

contatos2.setdefault("say@20202", "geovana")
print(contatos2)

# atualizar o dicionario
contatos2.update({ "say@2020": {"nome": "cris"} })
contatos2.update({ "crats": {"nome": "bsgdvd", "idade": 20} })
print(contatos2)

# retorna só o valor
print(contatos2.values())

# verifia se está presente no dicionario
print("cris@2020" in contatos2)

# apagar valor 
del contatos2["cris@2020"]
del contatos2["cristovam@2020"]["telefone"]
print(contatos2)