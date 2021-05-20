#     8. (DESAFIO) Escreva um programa que determine todos os números de 4 algarismos que possam ser separados em dois números de dois algarismos que somados e elevando-se a soma ao quadrado obtenha-se o próprio número.

# Exemplo: 3025 = 55 e 55**2 é igual á 3025
n = []
soma_algarismo = 0
for item in range(1000, 9999):
    centena = item // 100
    dezena = item % 100
    soma_algarismo = centena + dezena
    if soma_algarismo ** 2 == item:
        n.append(item)
print(
    f'separados em dois números de dois algarismos que somados e elevando-se a soma ao quadrado obtenha-se o próprio número são: {n}')
