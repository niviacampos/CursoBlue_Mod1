# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto,
# que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
# A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto, custo):
    taxaImposto = (taxaImposto*custo)/100
    valor_total = custo + taxaImposto
    return valor_total


taxaImposto = float(input('Taxa de imposto: '))
custo = float(input('Valor de custo: '))

x = somaImposto(taxaImposto, custo)
print(x)
