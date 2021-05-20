# 3. O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:

print('Preço do pão: R$ 0.18')
print('Panificadora Pão de Ontem - Tabela de preços')

for item in range(1, 51):
    print(f'{item} - R$ {item * 0.18:.2f}')
