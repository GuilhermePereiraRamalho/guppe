"""
Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule
a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido
"""


x: int = int(input("Informe um número inteiro: "))

if x > 0:
    sqrt: float = x ** (1/2)
    print(f'A raíz quadrada de {x} é: {sqrt}')
elif x < 0:
    print('Número inválido!')
