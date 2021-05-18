# Dada uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte quantas vezes aparece uma vogal.

frase = input("Digite uma frase: \n")
vogais = []
num_vogais = 0

for item in frase:
    if item in 'aeiou':
        vogais.append(item)
print(f'Na frase {frase}:\n')
print(f'Vogal "a" aparece {vogais.count("a")} vezes')
print(f'Vogal "e" aparece {vogais.count("e")} vezes')
print(f'Vogal "i" aparece {vogais.count("i")} vezes')
print(f'Vogal "o" aparece {vogais.count("o")} vezes')
print(f'Vogal "u" aparece {vogais.count("u")} vezes')
