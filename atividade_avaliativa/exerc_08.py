# 08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade, com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

from datetime import date

trabalhador = {}

trabalhador['Nome'] = input('Digite seu nome: ')
trabalhador['Ano_Nasc'] = int(input('Ano nascimento: '))
trabalhador['CTPS'] = input('Número da CTPS: ')
trabalhador['Idade'] = date.today().year - trabalhador['Ano_Nasc']

if trabalhador['CTPS'] != '0':
    trabalhador['Ano_contratacao'] = int(input('Ano de contratação: '))
    trabalhador['Salario'] = float(
        input('Valor do salário: R$ ')).replace(',', '.')
    trabalhador['Aposentadoria'] = 35 - (date.today(
    ).year - trabalhador['Ano_contratacao'])
else:
    print('CTPS não cadastrada. Não é possível calcular o ano de aposentadoria.')

print()
print('-=-' * 10)
print('   Dados do Trabalhador:')
print('-=-' * 10)
for key, values in trabalhador.items():
    print(f'{key}: {values}')
