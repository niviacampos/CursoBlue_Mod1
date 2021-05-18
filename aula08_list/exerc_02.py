''' 2. Faça um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
'''

import random

palavras = input("Digite palavras: ").lower().split(" ")
# sorteada1 = random.randrange(len(palavras)) ISSO FUNCIONA MESMO PRA STRING???
sorteada = random.choice(palavras)
palavra_forca = ['_ ' for i in sorteada]

letras = []

max_tentativas = len(sorteada) + 6
tentativas = 0
print('= '*30)
print(f'Vamos jogar forca? Você possui {max_tentativas} chances.')
print('= '*30)

for item in range(max_tentativas):
    if palavra_forca.count('_ ') == 0 or tentativas == 6:
        break

    letra = input('Digite uma letra \n').lower()[0]

    if letra in palavra_forca or letra in letras:
        print(f'Você já digitou essa letra antes.')
        continue

    if letra in sorteada:
        for i in range(len(sorteada)):
            if letra == sorteada[i]:
                del palavra_forca[i]
                palavra_forca.insert(i, letra)
    else:
        letras.append(letra)
        tentativas += 1
        print('Não tem essa letra na palavra escolhida\n')
        print(f'Você só pode errar mais {6-tentativas} vezes.\n')

if palavra_forca.count('_ ') == 0:
    print('Você GANHOU!!!')
elif tentativas == 6:
    print('Você PERDEU! =( ... Estrapolou o número de tentativas.')

print(
    f'A palavra correta é "{" ".join(sorteada)}"\nVocê acertou as letras {palavra_forca}\nErrou as letras {letras}')
