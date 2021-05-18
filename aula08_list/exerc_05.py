# Desenvolva um código que pergunte um número n para o usuário e exiba todos seus divisores. Caso seja um número primo, o programa ainda deve informar que se trata de um número primo!

divisores = []
num = int(input('Digite um número:'))

for item in range(1, num+1):
    if num % item == 0:
        divisores.append(item)
if len(divisores) > 2:
    print(f'O número {num} NÃO  é primo!')
else:
    print(f'O número {num} é primo!')

print(f'Seus divisores são: {divisores}')
