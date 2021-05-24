# 03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar seu processamento, só deixe o usuário continuar se a senha estiver correta, após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, onde o computador vai “pensar” em um número inteiro entre 0 e 20. O jogador vai tentar adivinhar qual número foi escolhido até acertar, a cada palpite do usuário diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou, no final mostre quantos palpites foram necessários para vencer.

from random import randint

senha = 'senha@123'
senha_user = ''

while senha_user != senha:
    senha_user = input('Digite sua senha: ')

print('Olá, seja bem vindo!!!\nEsse é um jogo de advinhação, vou escolher um número entre 1 a 20 e você terá que descobrir qual número é este.\nVamos lá!?')
print()

num_sorteado = randint(1, 20)
num_user = tentativas = 0

while num_sorteado != num_user:
    tentativas += 1
    num_user = int(input('Adivinhe o número escolhido: '))
    if num_user > num_sorteado:
        print('Digite um número menor')
    elif num_user < num_sorteado:
        print('Digite um número maior.')
    else:
        print('Você acertou!!!')
print(f'Foram necessárias {tentativas} tentativas para você acertar.')
