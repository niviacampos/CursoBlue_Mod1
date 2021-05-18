# DESAFIO -  Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida. Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro terá 29 dias.

from datetime import datetime


def data_por_extenso(data):
    data2 = datetime.strftime(data, '%d/%B/%Y')
    print(data2)


data = input('Digite a data (DD/MM/AAAA): ')
data_extenso = datetime.strptime(data, '%d/%m/%Y')
datas = data_por_extenso(data_extenso)

# O RETORNO DO MÊS ESTÁ EM INGLÊS, COMO RETORNAR EM PORTUGUÊS?
