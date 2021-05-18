# EXERCÍCIOS AULA 6
# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(x, y, z):
    adicao = x + y + z
    print(f'O resultado da sua soma é: {adicao}')
    return adicao


x1 = int(input('Digite o 1º número: '))
y1 = int(input('Digite o 2º número: '))
z1 = int(input('Digite o 3º número: '))
soma(x1, y1, z1)
