from collections import Counter

texto1 = """
Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus et quia sint sapiente sunt quas, enim sequi nulla accusamus ipsam consequatur deleniti repellat quisquam dignissimos omnis delectus, velit ullam quod.
Lorem ipsum dolor, sit amet consectetur adipisicing elit. Doloremque laboriosam fugit asperiores nisi reprehenderit explicabo dolores delectus incidunt consectetur? Eum, et. Sequi quaerat, eos optio blanditiis modi accusantium ex consectetur!
Lorem ipsum dolor sit amet consectetur adipisicing elit. Laborum consequuntur dolor eos mollitia maxime aliquid, quia officiis doloremque eligendi quam ex officia. Doloremque nulla distinctio debitis animi tenetur voluptatum delectus.
"""
texto2 = """
Lorem ipsum dolor sit amet consectetur adipisicing elit. Id similique suscipit ipsam nisi consectetur tempore dolorum eligendi error non quisquam alias doloremque quasi ullam, magni modi harum numquam. Id, dicta!
Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ab, repellendus! Dignissimos adipisci amet fuga placeat similique, pariatur doloribus nulla libero nesciunt hic labore nihil expedita natus, architecto quaerat et nobis.
Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae commodi odit in, amet voluptatibus vel incidunt esse dolor modi repudiandae molestias aut sunt nam! Quisquam numquam mollitia ab vero illum.
"""

for x in "Lorem":
    print(x)

def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    # print(aparicoes)
    total_caracteres = sum(aparicoes.values())
    # for letra, frequencia in aparicoes.items():
    #     tupla = (letra, frequencia / total_caracteres)
    #     print(tupla)
    proporcoes = [(letra, frequencia / total_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, proporcao * 100))
analisa_frequencia_de_letras(texto1)
analisa_frequencia_de_letras(texto2)
