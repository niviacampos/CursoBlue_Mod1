# Exercício 5 - Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros: o nome de um jogador e quantos gols ele marcou.

# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(jogador, gols):
    print(jogador, gols)
    return jogador, gols


jogador = input("Nome do jogador: ")
gols = int(input('Total de gols: '))

ficha_jogador = ficha(jogador, gols)
