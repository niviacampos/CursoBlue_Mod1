# # 3. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# # • "Telefonou para a vítima?"
# # • "Esteve no local do crime?"
# # • "Mora perto da vítima?"
# # • "Devia para a vítima?"
# # • "Já trabalhou com a vítima?"
# # O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?",
             "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]

sim = 0

for item in perguntas:
    print(item)
    resposta = input('Responda Sim ou Não: ').lower()[0]
    print(resposta)
    if resposta == 's':
        sim += 1
    if sim == 5:
        print('Assinano')
    elif sim == 3 or sim == 4:
        print('Cúmplice')
    elif sim == 2:
        print('Suspeito')
    else:
        print('Inocente')
    print(f'{sim} respostas positivas')


# r1 = int(input('Telefonou para a vítima? [1] Sim [0] Não:'))
# r2 = int(input('Esteve no local co crime? [1] Sim [0] Não:'))
# r3 = int(input('Mora perto da vítima? [1] Sim [0] Não:'))
# r4 = int(input('Devia para a vítima? [1] Sim [0] Não:'))
# r5 = int(input('Já trabalhou com a vítima? [1] Sim [0] Não:'))

# lista = [r1, r2, r3, r4, r5]

# if sum(lista) == 2:
#     print('SENTENÇA:SUSPEITO!')
# elif sum(lista) == 3 or sum(lista) == 4:
#     print('SENTENÇA:CÚMPLICE!')
# elif sum(lista) == 5:
#     print('SENTENÇA:ASSASSINO!')
# else:
#     print('SENTENÇA:INOCENTE!')
