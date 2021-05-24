# 02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma string com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.

# Armazenando as vogais em lista e realizando o count
frase = input('Digite uma frase: ').lower()

vogais_frase = []
frase_sem_vogal = []

for item in frase:
    if item in "aeiou":
        vogais_frase.append(item)
    else:
        frase_sem_vogal.append(item)

print(f'A vogal "a" aparece {vogais_frase.count("a")} vezes')
print(f'A vogal "e" aparece {vogais_frase.count("e")} vezes')
print(f'A vogal "i" aparece {vogais_frase.count("i")} vezes')
print(f'A vogal "o" aparece {vogais_frase.count("o")} vezes')
print(f'A vogal "u" aparece {vogais_frase.count("u")} vezes')

print(
    f'Sem as vogais a frase ficaria da seguinte forma: {"".join(frase_sem_vogal)}')


# # Utilizando estruturas condicionais ao invés da função count de lista

# frase = input('Digite uma frase: ')

# vogal_a = vogal_e = vogal_i = vogal_o = vogal_u = 0
# frase_sem_vogal = []

# for item in frase:
#     if item not in "aeiou":
#         frase_sem_vogal.append(item)
#     if item == 'a':
#         vogal_a += 1
#     elif item == 'e':
#         vogal_e += 1
#     elif item == 'i':
#         vogal_i += 1
#     elif item == 'o':
#         vogal_o += 1
#     elif item == 'u':
#         vogal_u += 1


# print(
#     f'Cada vogal é exibida na frase:\nVogal "a" {vogal_a} vezes\nVogal "e" {vogal_e} vezes\nVogal "i" {vogal_i} vezes\nVogal "o" {vogal_o} vezes\nVogal "u" {vogal_u} vezes\n')
# print(f'Sem as vogais, a frase seria: {"".join(frase_sem_vogal)}')
