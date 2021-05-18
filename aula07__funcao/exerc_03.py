# Exercício Treino 3 - Crie uma função que receba uma string como argumento e retorne a mesma string em letras maiúsculas. Faça uma chamada à função, passando como parâmetro uma string.

def formatar_string(palavra):
    print(palavra)
    return palavra


palavras = input('Digite alguma palavra ou frase: ').upper()
a = formatar_string(palavras)
