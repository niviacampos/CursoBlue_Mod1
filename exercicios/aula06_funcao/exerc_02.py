#  Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
# se seu argumento for positivo, ‘N’, se seu argumento for negativo e ‘0’ se for 0.

def positivo_negativo_neutro(numero):
    if numero == 0:
        print('0')
    if numero > 0:
        print('P')
    if numero < 0:
        print('N')

    return numero


n2 = int(input('Digite um número: '))
print(positivo_negativo_neutro(n2))
