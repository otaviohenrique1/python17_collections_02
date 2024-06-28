aparicoes = {
    "Guilherme": 1,
    "cachorro": 2,
    "nome": 2,
    "vindo": 1,
}
print(aparicoes)
print(type(aparicoes))
print(aparicoes["Guilherme"])
print(aparicoes["cachorro"])
aparicoes["Carlos"] = 2
print(aparicoes)
print("cachorro" in aparicoes)
print(aparicoes)
del aparicoes["Carlos"]
print(aparicoes)
print(aparicoes.get("cachorro", 0))
for elemento in aparicoes:
    print(elemento)
for elemento in aparicoes.keys():
    print(elemento)
for elemento in aparicoes.values():
    print(elemento)
for elemento in aparicoes.items():
    print(elemento)
for chave, valor in aparicoes.items():
    print(chave, "=", valor)
print(["palavra {}".format(chave) for chave in aparicoes.keys()])
aparicoes2 = dict(Guilherme=2, cachorro=1)
print(aparicoes2)
