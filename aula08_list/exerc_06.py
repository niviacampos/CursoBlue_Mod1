# Escreva um programa onde o usuário digita uma frase e essa frase retorna sem nenhuma vogal.

frase = input("Digite uma frase: ")
consoantes = []
num_vogais = 0
frase_sem_vogais = ''

for item in frase:
    if item not in 'aeiou':
        consoantes.append(item)
    else:
        num_vogais += 1
print(
    f'Sua frase sem vogais: {frase_sem_vogais}.\nForam removidas as consoantes: {num_vogais}')
