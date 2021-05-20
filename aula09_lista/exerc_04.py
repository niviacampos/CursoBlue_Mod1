# Crie um código em Python que receba uma lista de nomes informados pelo usuário com tamanho indefinido (a lista deve ser encerrada quando o usuário digitar 0) e, na sequência, receba um nome para que seja verificado se este consta na lista ou não. Observação: ignorar diferenças entre maiúsculas e minúsculas.

nomes = ''
lista_nomes = []

while nomes != '0':
    nomes = input('Digite o nome ou 0 (zero) para sair. ').title()
    if nomes not in lista_nomes:
        lista_nomes.append(nomes)
    else:
        print(f'O nome {nomes} já consta na lista.')
