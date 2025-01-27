'''
 Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar
'''


x: int = int(input("Informe um número inteiro: "))

if x % 2 == 0:
    print(f'Você digitou o número {x} e ele é par')
else:
    print(f'Você digitou o número {x} e ele é ímpar')
