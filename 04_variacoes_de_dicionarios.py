from collections import defaultdict, Counter

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()
aparicoes = defaultdict(int)
for palavra in meu_texto.split():
    aparicoes[palavra] += 1
print(aparicoes)


class Conta:
    def __init__(self):
        print("Criando uma conta")

contas = defaultdict(Conta)
print(contas[17])

aparicoes2 = Counter(meu_texto.split())
print(aparicoes2)