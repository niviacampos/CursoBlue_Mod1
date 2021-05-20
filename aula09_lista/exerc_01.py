# Crie um código em Python que pede qual tabuada o usuário quer ver, em seguida imprima essa tabuada.

numero_tabuada = int(input('Deseja efetuar a tabuada de qual número? '))

# for item in range(0, 11):
#     tabuada = numero_tabuada * item
# print(f'{item} x {numero_tabuada} = {tabuada}')

print([numero_tabuada * item for item in range(0, 11)])
