# Crie um código em Python para exibir a contagem de dígitos de um número inteiro positivo informado pelo usuário.

numero = int(input('Digite um valor positivo: '))

if numero >= 0:
    numero = str(numero)
    print(f'O número {numero} possui {len(numero)} dígitos.')
else:
    print('Digite um valor positivo.')
