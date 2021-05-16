# Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário é pago conforme a quantidade de horas
# trabalhadas. Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.

def salarios(horas, salario_hora):
    if horas > 40:
        horas = horas_totais - 40
        salario_total = (salario_hora * 40) * 1.5 * horas
        print(
            f'Total de horas trabalhadas: {horas_totais}\n Valor da hora trabalhada: {valor_por_hora}\nHora extra: {horas}\nSalário total: {salario_total}')
    else:
        salario_total = salario_hora * 40
        print(
            f'Total de horas trabalhadas: {horas_totais}\n Valor da hora trabalhada: {valor_por_hora}\nSalário total: {salario_total}')
    return salario_total


valor_por_hora = float(input('Valor por hora trabalhada: R$ '))
horas_totais = float(input('Total de horas trabalhadas: '))
a = salarios(horas_totais, valor_por_hora)
print(a)
