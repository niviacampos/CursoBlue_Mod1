def custo_hotel(noites):
    return noites * 140


def custo_aviao(cidade):
    passagem = 0
    if cidade == 'são paulo' or cidade == 'sao paulo':
        passagem = 312
    elif cidade == 'porto alegre':
        passagem = 447
    elif cidade == 'recife':
        passagem = 831
    elif cidade == 'manaus':
        passagem = 986
    else:
        print('Não temos passagem para essa cidade. Temos disponíveis São Paulo, Porto Alegre, Recife e Manaus')
    return passagem


# custo_passagem = custo_aviao(destino)


def custo_carro(dias):
    custo_car = 0
    if dias >= 3 and dias < 7:
        custo_car = dias * 40 - 20
    elif dias >= 7:
        custo_car = dias * 40 - 50
    else:
        custo_car = dias * 40
    return custo_car


def calculo_total(custo_hospedagem, passagem, custo_car,  gastos_extras):

    total_hotel = custo_hotel(custo_hospedagem)
    total_passagem = custo_aviao(passagem)
    total_carro = custo_carro(custo_car)
    custo_total = total_hotel + total_passagem + total_carro + gastos_extras
    print(
        f'O custo total de uma viagem de {noites_hospedadas} dias para{destino} gastando R$ {gastos_extras} adicionais é {custo_total}')
    return custo_total


noites_hospedadas = int(input('Quantas noites ficará hospedado? '))
destino = input('Qual o seu destino? ').lower()
carro = int(input('Por quantos dias alugará o carro? '))
gastos_extras = int(input('Gastos extras: '))

total_viagem = calculo_total(noites_hospedadas, destino, carro, gastos_extras)


# Exiba no console o custo total de uma viagem de 12 dias para 'Manaus' gastando R$ 800,00 adicionais.
