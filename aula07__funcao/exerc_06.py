# Exercício 6

# Um professor, muito legal, fez 3 provas durante um semestre, mas só vai levar em conta as duas notas mais altas para calcular a média.

# Faça uma aplicação que peça o valor das 3 notas, mostre como seria a média com essas 3 provas, a média com as 2 notas mais altas, bem como sua nota mais alta e sua nota mais baixa.

# maiores_notas recebe a lista c/ todas as      notas, ordena de forma crescente e remove o menor valor para realizar a média das maiores notas.

def notas(notas_avs):
    media_2notas = media_3notas = maiores_notas = 0
    maior_nota = max(notas_avs)
    menor_nota = min(notas_avs)
    media_3notas = sum(notas_avs)/3
    maiores_notas = notas_avs.copy()
    maiores_notas.sort()
    maiores_notas.pop(0)
    media_2notas = sum(maiores_notas)/2

    print('media2', media_2notas)
    if media_2notas < media_3notas:
        print(
            f'Será considerada a média das três notas {notas_avs}, no total de {media_3notas}')
    else:
        print(
            f'Será considerada a média das duas maiores notas {maiores_notas}, no total de {media_2notas}')

    print(f'Nota mais alta = {maior_nota}\nNota mais baixa = {menor_nota}')
    return maior_nota, menor_nota, media_2notas, media_3notas


notas_avs = []
for item in range(3):
    nota = float(input(f'Nota avaliação{[item+1]}: '))
    notas_avs.append(nota)

lancamento_notas = notas(notas_avs)
