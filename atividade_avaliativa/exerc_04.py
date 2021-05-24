# 04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Valide a data e retorne NULL caso a data seja inválida.

# Usando lista no input da data
def data():
    data_usuario = list(input('Digite a data (dd/mm/aaaa): '))
    mes_extenso = data_usuario[3:5]

    if '0' in mes_extenso[0] and '1' in mes_extenso[1]:
        mes_extenso = 'Janeiro'
    elif '0' in mes_extenso[0] and '2' in mes_extenso[1]:
        mes_extenso = 'Fevereiro'
    elif '0' in mes_extenso[0] and '3' in mes_extenso[1]:
        mes_extenso = 'Março'
    elif '0' in mes_extenso[0] and '4' in mes_extenso[1]:
        mes_extenso = 'Abril'
    elif '0' in mes_extenso[0] and '5' in mes_extenso[1]:
        mes_extenso = 'Maio'
    elif '0' in mes_extenso[0] and '6' in mes_extenso[1]:
        mes_extenso = 'Junho'
    elif '0' in mes_extenso[0] and '7' in mes_extenso[1]:
        mes_extenso = 'Julho'
    elif '0' in mes_extenso[0] and '8' in mes_extenso[1]:
        mes_extenso = 'Agosto'
    elif '0' in mes_extenso[0] and '9' in mes_extenso[1]:
        mes_extenso = 'Setembro'
    elif '1' in mes_extenso[0] and '0' in mes_extenso[1]:
        mes_extenso = 'Outubro'
    elif '1' in mes_extenso[0] and '1' in mes_extenso[1]:
        mes_extenso = 'Novembro'
    elif '1' in mes_extenso[0] and '2' in mes_extenso[1]:
        mes_extenso = 'Dezembro'

    else:
        print('Data inválida. Tente novamente.')
        return

    data_extenso = (
        f'{"".join(data_usuario[:2])} {mes_extenso} de {"".join(data_usuario[6:])}')
    print(data_extenso)
    return print(data_extenso)


data()


# Recebendo a data por dia, mês e ano


# def data(dia, mes, ano):
#     dia = int(dia)
#     ano = int(ano)

#     if dia > 31:
#         print("Dia inválido.")
#     elif mes == '04' or mes == '06' or mes == '09' or mes == '11' and dia > 30:
#         print(f'INVÁLIDO! O mês {mes} possui 30 dias.')
#     elif mes == '02' and dia > 28 and ano % 4 != 0:
#         print('Dia inválido.')
#     else:
#         if mes == '01':
#             mes = 'Janeiro'
#         elif mes == '02':
#             mes = 'Fevereiro'
#         elif mes == '03':
#             mes = 'Março'
#         elif mes == '04':
#             mes = 'Abril'
#         elif mes == '05':
#             mes == 'Maio'
#         elif mes == '06':
#             mes = 'Junho'
#         elif mes == '07':
#             mes = 'Julho'
#         elif mes == '08':
#             mes = 'Agosto'
#         elif mes == '09':
#             mes = 'Setembro'
#         elif mes == '10':
#             mes == 'Outubro'
#         elif mes == '11':
#             mes = 'Novembro'
#         elif mes == '12':
#             mes = 'Dezembro'
#         else:
#             print('Mês inválido.')
#             # como faz o retorno Null? Seria só "return"
#             return {mes: 'NULL'}

#         print(f'{dia} de {mes} de {ano}')
#         return [dia, mes, ano]


# dd = input("Digite o dia (dd): ")[:2]
# mm = input('Digite o mês (mm): ')[:2]
# aaaa = input('Digite o ano (aaaa): ')[:4]

# data(dd, mm, aaaa)


# USANDO DATETIME
# from datetime import date, datetime


# def data():
#     data_usuario = input('Digite a data (dd/mm/aaaa): ')
#     try:  # Não consegui validar com if/else
#         data_usuario = datetime.strptime(data_usuario, '%d/%m/%Y')
#         data_extenso = datetime.strftime(data_usuario, '%d,%B,%Y')
#         print(data_extenso)
#         return data_extenso

#     except:
#         print('Data inválida!')
#         return


# data()
