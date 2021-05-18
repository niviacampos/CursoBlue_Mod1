# 6. Escreva uma função que, dado um número nota representando a nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).

# Nota/Conceito
# >=9.0 A
# >=8.0 B
# >=7.0 C
# >=6.0 D
# <=4.0 F   AQUI NÃO SERIA <=5?

def notas(nota, conceito):
    if nota >= 9:
        conceito = 'A'
    elif nota >= 8:
        conceito = 'B'
    elif nota >= 7:
        conceito = 'C'
    elif nota >= 6:
        conceito = 'D'
    elif nota >= 5:
        conceito = 'E'
    else:
        conceito = 'f'
    print(f'{aluno} possui nota = {nota} e conceito = {conceito}.')
    return nota, conceito


aluno = input('Nome do aluno(a): ')
avaliacao = float(input('Digite a nota do aluno(a): '))
conceito = ''
notas_conceitos = notas(avaliacao, conceito)
