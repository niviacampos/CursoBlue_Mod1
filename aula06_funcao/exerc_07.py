# Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem iguais, imprima que eles são iguais.

def menor_num(num1, num2):
    menor = num1
    if num1 < num2:
        print(f'O menor número digitado é {menor}.')
    elif num1 == num2:
        print(f'Os números digitados são iguais {num1}.')
    else:
        print(f'O menor número digitado é {num2}')
    return menor


n1 = int(input('Digite um número: '))
n2 = int(input('Digite o segundo número: '))
numeros = menor_num(n1, n2)
