# 07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

numeros = [[], []]  # Lista única pode ser uma lista com dois elementos?

for item in range(1, 8):
    numero = int(input(f'Digite o valor {item}: '))

    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

numeros[0].sort()
numeros[1].sort()

print(
    f'Os números pares são: \t{numeros[0]}\nOs números ímpares são: {numeros[1]}')
