# Exercício Treino 2 - Escreva uma função que recebe dois números (a e b) como parâmetro e retorna True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.

def validacao_numeros(a, b, limite):
    numero = a + b
    if numero < limite:
        print(f'O terceiro número ({limite}) é maior que a soma de {a} e {b}.')
        return True
    else:
        print(
            f'A soma de {a} e {b} é maior que o terceiro número informado ({limite}.)')


num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))

numeros = validacao_numeros(num1, num2, num3)
