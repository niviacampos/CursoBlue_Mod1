# Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.

def calculo_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc


kg = float(input("Qual o seu peso? ").replace(',', '.'))
h = float(input("Qual a sua altura? ").replace(',', '.'))

calc_imc = calculo_imc(kg, h)
print(f'Seu imc é {calc_imc:.2f}')
