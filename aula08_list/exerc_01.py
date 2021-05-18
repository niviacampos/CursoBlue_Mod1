# 1. Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
#     a. tamanho da lista.
#     b. maior valor da lista.
#     c. menor valor da lista.
#     d. soma de todos os elementos da lista.
#     e. lista em ordem crescente.
#     f. lista em ordem decrescente.

l = [5, 7, 2, 9, 4, 1, 3]
a = len(l)
print(a)
b = max(l)
print(b)
c = min(l)
print(c)
d = sum(l)
print(d)
l.sort()
e = l
print(e)
l.reverse()
f = l
print(f)
