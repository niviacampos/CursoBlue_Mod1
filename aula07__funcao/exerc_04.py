# Exercício 4 - Crie um programa que tenha uma função chamada voto () que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições. Para resolver esse exercício, pesquise sobre a função date da biblioteca Datetime.

from datetime import datetime, date

# now_a = datetime.now()
# # now_a = datetime.strftime(now_a, '%Y')
# year_now = (now_a).year
# print(year_now)
# print(type(now_a))


def direito_voto(ano_nasc):
    idade = date.today().year - ano_nasc
    print(type(idade))
    if idade >= 16 and idade < 18 or idade >= 65:
        print('Voto OPCIONAL')
    elif idade >= 18:
        print('Voto OBRIGATÓRIO')
    else:
        print('Voto NEGADO')
    return idade


nascimento = int(input('Informe seu ano de nascimento: '))
voto = direito_voto(nascimento)
