# (DESAFIO) Desenvolva um código em Python que gere um número aleatório de 1 a 100 e dê ao usuário 10 chances para acertá-lo. A cada tentativa, deve ser impressa a quantidade de tentativas restantes e se o número aleatório é maior ou menor do que o número inserido na tentativa atual. Se o usuário não acertar em 10 tentativas, informe qual o número aleatório. [Dica: use a função randint para gerar o número aleatório]

from random import randint

num_aleatorio = randint(1, 100)

for item in range(10):
    num_user = int(
        input(f'Você possui {10 - item} tentativas para acertar o número: '))
    if num_user > num_aleatorio:
        print('Você errou! O número escolhido é menor que ', num_user)
    elif num_user < num_aleatorio:
        print('Você errou! O número escolhido é maior que ', num_user)
    else:
        print('Você GANHOU')
print(f'Número escolhido é {num_aleatorio}')
