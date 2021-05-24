# 05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e retorne o resultado. Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.

def vogais_na_frase(frase):
    lista_vogais = []
    frase_sem_vogais = []
    for item in frase_usuario:
        if item in "aeiou":
            lista_vogais.append(item)
        else:
            frase_sem_vogais.append(item)

    print(f'A vogal "a" aparece {lista_vogais.count("a")} vezes.')
    print(f'A vogal "e" aparece {lista_vogais.count("e")} vezes.')
    print(f'A vogal "i" aparece {lista_vogais.count("i")} vezes.')
    print(f'A vogal "o" aparece {lista_vogais.count("o")} vezes.')
    print(f'A vogal "u" aparece {lista_vogais.count("u")} vezes.\n')

    print(f'O total de letras removidas é {len(lista_vogais)}\n')

    print(f'Sem as vogais a frase seria: "{"".join(frase_sem_vogais)}"')


frase_usuario = input('Digite uma frase: ').lower()
vogais_na_frase(frase_usuario)
