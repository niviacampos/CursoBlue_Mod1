# Faça um script que peça ao usuário o número de matérias da escola, ou seja, um inteiro positivo. Em seguida, ele vai digitando o valor de cada nota, de cada matéria e isso será armazenado numa lista. Ao final, seu script deverá fornecer a média geral do aluno.

num_materias = int(input('Quantas matérias da escola? '))
notas_totais = []

for i in range(num_materias):
    notas = float(input(f'Digite a nota da matéria {i+1}: '))
    notas_totais.append(notas)
    media_notas = sum(notas_totais)/len(notas_totais)
print('Média total = ', media_notas)
