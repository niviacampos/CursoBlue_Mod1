# 06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
#  "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

perguntas = ["Telefonou para a vítima?",
             "Esteve no local do crime?",
             "Mora perto da vítima?",
             "Devia para a vítima?",
             "Já trabalhou com a vítima?"]

s = n = 0
resp_invalida = []

for item in range(len(perguntas)):
    respostas = input(f'{perguntas[item]} Sim ou Não? ').title()[0]
    if respostas == 'S':
        s += 1
    elif respostas == 'N':
        n += 1
    else:
        resp_invalida.append(perguntas[item])
        print('Resposta inválida')
        print(resp_invalida)
        for i in range(len(resp_invalida)):
            while respostas != 'S' or 'N':
                respostas = input(
                    f'Responda novamente. {resp_invalida[i]} Sim ou Não? ').title()[0]
                break
if s == 5:
    print('Assassino.')
elif s == 3 or s == 4:
    print('Cúmplice.')
elif s == 2:
    print('Suspeito.')
else:
    print('Inocente.')
