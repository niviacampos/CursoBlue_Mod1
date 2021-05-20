# 5. O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

prod_comprado = []
produtos = 0

print('LOJAS TABAJARA')

while True:
    valor_produto = float(input('Valor do produto: '))
    produtos += 1
    prod_comprado.append(valor_produto)
    if valor_produto == 0:
        break
    print(f'Produto {produtos}: R$ {valor_produto}')
total = sum(prod_comprado)
dinheiro = float(input('Dinheiro: R$ '))
troco = dinheiro - total
print(f'Total: R$ {total}\nDinheiro: R$ {dinheiro}\nTroco: R${troco}')
