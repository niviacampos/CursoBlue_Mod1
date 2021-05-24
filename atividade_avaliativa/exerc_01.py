# 01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
# A soma deles;
# A multiplicação entre eles;
# A divisão inteira deles;
# Mostre na tela qual é o maior;
# Verifique se o resultado da soma é par ou impar e mostre na tela;
# Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

soma = numero1 + numero2
print(f'A soma entre {numero1} e {numero2} = {soma}')
multiplicacao = numero1 * numero2
print(f'A multiplicação entre {numero1} e {numero2} = {multiplicacao}')
divisao = numero1 // numero2
print(f'A divisão inteira entre {numero1} e {numero2} = {divisao}')

# maior número
if numero1 > numero2:
    print(f'O número {numero1} é maior que {numero2}.')
elif numero1 < numero2:
    print(f'O número {numero2} é maior que {numero1}.')
else:
    print(f'os números {numero1} e {numero2} são iguais.')

# Soma par ou ímpar
if soma % 2 == 0:
    print(
        f'O resultado da soma entre os números {numero1} e {numero2} é {soma}. Logo, o resultado da soma "{soma}" é par.')
else:
    print(
        'O resultado da soma entre os números {numero1} e {numero2} é {soma}. Logo, o resultado da soma "{soma}" é ímpar.')

# Multiplicação > 40 faz a divisão
if multiplicacao > 40:
    mult_div = multiplicacao // divisao
    print(f'O número {multiplicacao} dividido por {divisao} é {mult_div}.')
else:
    print(f'A multiplicação dos números {numero1} e {numero2} é menor que 40.')
